from django import forms
from app_cw.utils.bootstrap import BootStrapModelForm
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from app_cw import models
class UserModelForm(BootStrapModelForm):
    name = forms.CharField(min_length=3, label="用户名")

    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age", "account", "create_time", "gender", "depart"]
        # 手动添加样式
        # widgets = {
        #     "name": forms.TextInput(attrs={"class": "form-control"}),
        #     "password": forms.PasswordInput(attrs={"class": "form-control"}),
        #     "age": forms.TextInput(attrs={"class": "form-control"}),
        # }


class PrettyModelForm(BootStrapModelForm):
    # 方式一校验
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误'), ]
    )

    class Meta:
        model = models.PrettyNum
        # fields = "__all__" 所有字段
        fields = ["mobile", "price", "level", "status"]
        # exclude = ['level'] 排除字段


    # 验证方式二
    def clean_mobile(self):
        txt_mobile = self.cleaned_data["mobile"]

        exists = models.PrettyNum.objects.filter(mobile=txt_mobile).exists()
        if exists:
            # 验证不通过
            raise ValidationError("手机号已存在")

        # 验证通过，用户输入的值返回
        return txt_mobile



class PrettyEditModelForm(BootStrapModelForm):
    # 方式一校验
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误'), ],
        # disabled = True
    )

    # mobile = forms.CharField(disabled=True, label="手机号")

    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price', 'level', 'status']


    # 验证方式二
    def clean_mobile(self):

        # 当前编辑的哪一行的ID
        # print(self.instance.pk)

        txt_mobile = self.cleaned_data["mobile"]

        exists = models.PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
        if exists:
            # 验证不通过
            raise ValidationError("手机号已存在")

        # 验证通过，用户输入的值返回
        return txt_mobile