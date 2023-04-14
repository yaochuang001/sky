from django.db import models


# Create your models here.


class LhData(models.Model):
    """龙华数据表"""
    # 想要允许为空 null=True, blank=True

    equipment_name = models.CharField(verbose_name="设备", max_length=64)
    serial_number = models.IntegerField(verbose_name="序列号")
    equipment_status = models.CharField(verbose_name="设备状态", max_length=64)
    sap_number = models.CharField(verbose_name="SAP工单号", null=True, blank=True, max_length=64)
    sky_number = models.CharField(verbose_name="创维编码", null=True, blank=True, max_length=64)
    product_name = models.CharField(verbose_name="产品名称", null=True, blank=True, max_length=64)
    work_order = models.IntegerField(verbose_name="工单数")
    total_output = models.IntegerField(verbose_name="总完工数")
    current_output = models.IntegerField(verbose_name="当班完工数")
    work_cycle = models.FloatField(verbose_name="当前周期")
    delay_worktime = models.FloatField(verbose_name="总误时")
    pickup_method = models.CharField(verbose_name="取件方式", null=True, blank=True, max_length=64)


class LhWorkStatus(models.Model):
    """龙华工作状态数量"""
    c_time = models.DateTimeField('刷新时间', auto_now_add=True)
    work = models.IntegerField(verbose_name="生产中")
    stop = models.IntegerField(verbose_name="停机中")
    plan_stop = models.IntegerField(verbose_name="计划停机")
    test = models.IntegerField(verbose_name="调机中")
    other = models.IntegerField(verbose_name="其他", null=True, blank=True)
    work_proportion = models.FloatField(verbose_name="实时开机率")


class RobotData(models.Model):
    """注塑机械手实时参数"""
    c_time = models.DateTimeField('刷新时间', auto_now_add=True)
    sys_status = models.IntegerField(verbose_name="系统状态", default=0)
    work_status = models.IntegerField(verbose_name="运行状态", default=0)
    work_order = models.IntegerField(verbose_name="工单数", default=0)
    work_error = models.IntegerField(verbose_name="报警代码", default=0)
    work_output = models.IntegerField(verbose_name="当前产量", default=0)
    total_output = models.IntegerField(verbose_name="总产量", default=0)
    x_speed = models.FloatField(verbose_name="X轴设置速度", default=0)
    y_speed = models.FloatField(verbose_name="Y轴设置速度", default=0)
    z_speed = models.FloatField(verbose_name="Z轴设置速度", default=0)
    c_speed = models.FloatField(verbose_name="C轴设置速度", default=0)
    r_speed = models.FloatField(verbose_name="R轴设置速度", default=0)


class RobotStatus(models.Model):
    """注塑机工作状态数量"""
    c_time = models.DateTimeField('刷新时间', auto_now_add=True)
    work = models.IntegerField(verbose_name="生产中")
    stop = models.IntegerField(verbose_name="停机中")
    test = models.IntegerField(verbose_name="调机中")
    work_error = models.IntegerField(verbose_name="报警中")
    work_proportion = models.FloatField(verbose_name="实时开机率")
    error_proportion = models.FloatField(verbose_name="实时报警")
    time = models.CharField('时间', max_length=20, unique=True)  # 作为唯一索引更新每天数据
    op_everyday = models.IntegerField('每日总产', default=0)
    # efficiency_avg = models.FloatField('平均效率', default=0)
    op_plane = models.IntegerField('计划产量', default=0)


class DgData(models.Model):
    """注塑机实时参数"""
    c_time = models.DateTimeField(verbose_name='刷新时间', auto_now_add=True)
    name = models.CharField(verbose_name="设备名称", max_length=64)
    sys_status = models.IntegerField(verbose_name="系统状态", default=0)
    total_output = models.IntegerField(verbose_name="总产量", default=0)
    efficiency = models.FloatField(verbose_name="当前节拍", default=0)


class DgStatus(models.Model):
    """注塑机每日工组状态"""
    name = models.CharField(verbose_name="设备名称", max_length=64, default='')
    c_time = models.DateTimeField('刷新时间', auto_now_add=True)
    work = models.IntegerField(verbose_name="生产中")
    stop = models.IntegerField(verbose_name="停机中")
    op_everyday = models.IntegerField('每日总产', default=0)
    efficiency_avg = models.FloatField('平均节拍', default=0)
    time = models.CharField('时间', max_length=20, default='2023-04-12')
