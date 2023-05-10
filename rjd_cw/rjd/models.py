from django.db import models


# Create your models here.
class CustomInfo(models.Model):
    """客户表"""
    company_name = models.CharField(verbose_name='公司名称', max_length=32,unique=True)
    contact_person = models.CharField(verbose_name='联系人', max_length=16)
    mobile = models.CharField(verbose_name='手机号', max_length=11)
    address = models.CharField(verbose_name='地址', max_length=64)

    def __str__(self):
        return self.company_name


class Supplier(models.Model):
    """供应商表"""
    supplier_name = models.CharField(verbose_name='供应商名', max_length=32,unique=True)
    contact_person = models.CharField(verbose_name='联系人', max_length=16)
    mobile = models.CharField(verbose_name='手机号码', max_length=11)
    address = models.CharField(verbose_name='地址', max_length=64)

    def __str__(self):
        return self.supplier_name


class PublicAccount(models.Model):
    """对公账目"""
    create_time = models.DateField(verbose_name="日期")
    type_choices = (
        (1, '货款'),
        (2, '报销单'),
        (3, '专项'),
    )
    type = models.SmallIntegerField(verbose_name='类型', choices=type_choices)
    supplier = models.ForeignKey(to="Supplier", to_field="supplier_name", null=True, blank=True,
                                 on_delete=models.SET_NULL)
    product_name = models.CharField(verbose_name='品名', max_length=64, null=True, blank=True)
    product_model = models.CharField(verbose_name='型号', max_length=16, null=True, blank=True)
    unit_price = models.DecimalField(verbose_name='单价', max_digits=10, decimal_places=2, null=True, blank=True)
    total_price = models.DecimalField(verbose_name='总价', max_digits=10, decimal_places=2)
    tax_choice = (
        (1, '是'),
        (2, '否'),
    )
    tax = models.SmallIntegerField(verbose_name='含税', choices=tax_choice)
    bill = models.CharField(verbose_name='发票备注', max_length=64, null=True, blank=True)


class PrivateAccount(models.Model):
    """对私账目"""
    create_time = models.DateField(verbose_name="日期")
    supplier = models.ForeignKey(to="Supplier", to_field="id", null=True, blank=True,
                                 on_delete=models.SET_NULL)
    product_name = models.CharField(verbose_name='品名', max_length=64, null=True, blank=True)
    unit_price = models.DecimalField(verbose_name='单价', max_digits=10, decimal_places=2, null=True, blank=True)
    total_price = models.DecimalField(verbose_name='总价', max_digits=10, decimal_places=2)
    remark = models.CharField(verbose_name='备注', max_length=128, null=True, blank=True)
    img = models.FileField(verbose_name="图片说明", max_length=128, upload_to='rjd/', null=True, blank=True)


class Unpaid(models.Model):
    """未付款账目"""
    create_time = models.DateField(verbose_name="日期")
    supplier = models.ForeignKey(to="Supplier", to_field="id", null=True, blank=True,
                                 on_delete=models.SET_NULL)
    product_name = models.CharField(verbose_name='品名', max_length=64, null=True, blank=True)
    quantity = models.CharField(verbose_name='数量', max_length=16, null=True, blank=True)
    total_price = models.DecimalField(verbose_name='总价', max_digits=10, decimal_places=2)
    paid = models.DecimalField(verbose_name='已付款', max_digits=10, decimal_places=2)
    final_payment= models.DecimalField(verbose_name='尾款', max_digits=10, decimal_places=2)
    tax_choice = (
        (1, '是'),
        (2, '否'),
    )
    tax = models.SmallIntegerField(verbose_name='含税', choices=tax_choice)
    bill = models.CharField(verbose_name='发票备注', max_length=64, null=True, blank=True)


class AccountsReceivable(models.Model):
    """应收款账目"""
    create_time = models.DateField(verbose_name="日期")
    custom = models.ForeignKey(to="CustomInfo", to_field="company_name", null=True, blank=True,
                                 on_delete=models.SET_NULL)
    product_name = models.CharField(verbose_name='品名', max_length=64, null=True, blank=True)
    product_model = models.CharField(verbose_name='型号', max_length=16, null=True, blank=True)
    quantity = models.CharField(verbose_name='数量', max_length=16, null=True, blank=True)
    total_price = models.DecimalField(verbose_name='总价', max_digits=10, decimal_places=2)
    paid = models.DecimalField(verbose_name='已付款', max_digits=10, decimal_places=2)
    final_payment = models.DecimalField(verbose_name='尾款', max_digits=10, decimal_places=2)