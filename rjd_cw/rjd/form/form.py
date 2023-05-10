from app_cw.utils.bootstrap import BootStrapModelForm
from django import forms
from rjd import models
from django.core.validators import RegexValidator


class CustomModelForm(BootStrapModelForm):
    company_name = forms.CharField(min_length=3, label="客户")
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误'), ]
    )

    class Meta:
        model = models.CustomInfo
        fields = ["company_name", "contact_person", "mobile", "address"]
        # fields = "__all__"


class SupplierModelForm(BootStrapModelForm):
    supplier_name = forms.CharField(min_length=3, label="供应商")
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误'), ]
    )

    class Meta:
        model = models.Supplier
        fields = ["supplier_name", "contact_person", "mobile", "address"]


class AccountPubModelForm(BootStrapModelForm):
    class Meta:
        model = models.PublicAccount
        fields = "__all__"


class AccountPriModelForm(BootStrapModelForm):
    bootstrap_exclude_fields = ['img']

    class Meta:
        model = models.PrivateAccount
        fields = "__all__"


class UnpaidModelForm(BootStrapModelForm):
    class Meta:
        model = models.Unpaid
        # fields = "__all__"
        exclude = ["final_payment"]

class AccountsReceivableModelForm(BootStrapModelForm):
    class Meta:
        model = models.AccountsReceivable
        # fields = "__all__"
        exclude = ["final_payment"]
