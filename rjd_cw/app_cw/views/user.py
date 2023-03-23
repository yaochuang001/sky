from django.shortcuts import render, redirect
from app_cw.utils.pagination import Pagination
from app_cw.form.form import *


# insert into app_cw_userinfo(name,password,age,account,create_time,gender,depart_id) values("菅含含","666",23,100.3,"2023-03-07",2,4);
# insert into app_cw_userinfo(name,password,age,account,create_time,gender,depart_id) values("姚闯","422423",23,200.3,"2023-03-05",1,5);
# insert into app_cw_userinfo(name,password,age,account,create_time,gender,depart_id) values("两千金","199128",23,300.3,"2023-03-3",2,6);
def user_list(request):
    """用户管理"""

    # 获取所有的用户列表
    queryset = models.UserInfo.objects.all()

    page_object = Pagination(request, queryset, page_size=2)
    """

    for obj in queryset:
        print(obj.id,obj.name,obj.account,obj.create_time.strftime("%Y-%m-%d"),obj.gender,obj.get_gender_display(),obj.depart_id,obj.depart.title)

    """
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
    }
    return render(request, 'user_list.html', context)


def user_add(request):
    """添加用户（原始方式）"""
    if request.method == "GET":
        context = {
            'gender_choices': models.UserInfo.gender_choices,
            'depart_list': models.Department.objects.all()
        }
        print(context)
        return render(request, 'user_add.html', context)

    # 获取用户提交的数据
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    age = request.POST.get('age')
    account = request.POST.get('ac')
    ctime = request.POST.get('ctime')
    gender_id = request.POST.get('gd')
    depart_id = request.POST.get('dp')

    # 添加到数据库
    models.UserInfo.objects.create(name=user, password=pwd, age=age,
                                   account=account, create_time=ctime,
                                   gender=gender_id, depart_id=depart_id)

    # 返回到用户列表页面
    return redirect("/user/list/")


#####################################################ModelForm 示例###########################################


def user_model_form_add(request):
    """添加用户（ModelForm版本）"""
    if request.method == "GET":
        form = UserModelForm()

        return render(request, 'user_model_form_add.html', {"form": form})

    # 用户POST提交数据，数据校验
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        # {'name': '小帅', 'password': 'afafa', 'age': 23, 'account': Decimal('8'), 'create_time': datetime.datetime(2022, 11, 23, 0, 0, tzinfo=backports.zoneinfo.ZoneInfo(y='UTC')), 'gender': 1, 'depart': <Department: 销售部>}
        # print(form.cleaned_data)
        # models.UserInfo.objects.create(...)
        form.save()
        return redirect("/user/list/")
    # 校验失败（在页面上显示错误信息）
    return render(request, 'user_model_form_add.html', {"form": form})


def user_edit(request, nid):
    """编辑用户"""
    # 根据ID去数据库获取要编辑的那一行数据（对象）
    row_object = models.UserInfo.objects.filter(id=nid).first()
    if request.method == "GET":
        form = UserModelForm(instance=row_object)
        return render(request, "user_edit.html", {'form': form})

    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    return render(request, 'user_edit.html', {'form': form})


def user_delete(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list/')