# Generated by Django 4.1.7 on 2023-03-27 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LhData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sap_number', models.CharField(blank=True, max_length=64, null=True, verbose_name='SAP工单号')),
                ('product_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='产品名称')),
                ('sky_number', models.CharField(blank=True, max_length=64, null=True, verbose_name='创维编码')),
                ('pickup_method', models.CharField(blank=True, max_length=64, null=True, verbose_name='取件方式')),
                ('work_order', models.IntegerField(verbose_name='工单数')),
                ('serial_number', models.IntegerField(verbose_name='序列号')),
                ('work_cycle', models.IntegerField(verbose_name='当前周期')),
                ('current_output', models.IntegerField(verbose_name='当班完工数')),
                ('total_output', models.IntegerField(verbose_name='总完工数')),
                ('delay_worktime', models.IntegerField(verbose_name='总误时')),
                ('equipment_name', models.CharField(max_length=64, verbose_name='设备')),
                ('equipment_status', models.CharField(max_length=64, verbose_name='生产中')),
            ],
        ),
    ]
