from django.shortcuts import render, redirect, HttpResponse

from django import forms

from app_cw.utils.bootstrap import BootStrapForm
from app_cw.utils.encrypt import md5
from app_cw import models
from app_cw.utils.code import check_code


class LoginForm(BootStrapForm):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput,
        required=True,  # 不能为空
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(render_value=True),
        required=True,
    )
    code = forms.CharField(
        label="验证吗",
        widget=forms.TextInput,
        required=True,
    )

    def clean_password(self):
        pwd = self.cleaned_data.get("password")

        return md5(pwd)


def login(request):
    """登陆"""
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        # 验证码校验
        user_input_code = form.cleaned_data.pop('code')  # 拿到code后将code从字典中剔除
        code = request.session.get('image_code', '')
        if code.upper() != user_input_code.upper():
            form.add_error("code", "验证码错误")
            return render(request, 'login.html', {'form': form})

        # 验证成功，获取到的用户名和密码
        # print(form.cleaned_data)
        # 去数据库校验用户名和密码是否正确
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("password", "用户名或密码错误")
            return render(request, 'login.html', {'form': form})

        # 用户名和密码正确
        # 网站生成随机字符串；写到用户浏览器的cookie中；再写入到session中：
        request.session["info"] = {'id': admin_object.id, 'name': admin_object.username}
        request.session.set_expiry(60 * 60 * 24 * 7)# 重新设置session超时时间

        return redirect('/sky/dg/chart/')
    return render(request, 'login.html', {"form": form})


from io import BytesIO


def image_code(request):
    """生成图片"""
    # 调用pillow的函数，生成图片
    img, code_string = check_code()

    # 写入到自己的session中，以便后续获取验证码再进行校验
    request.session['image_code'] = code_string
    # 给Session设置60s超时
    request.session.set_expiry(60)

    stream = BytesIO()
    img.save(stream, 'png')

    return HttpResponse(stream.getvalue())


def logout(request):
    """注销"""

    request.session.clear()

    return redirect('/login/')
