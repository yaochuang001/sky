# Generated by Django 4.1.7 on 2023-05-08 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rjd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='supplier_name',
            field=models.CharField(max_length=32, unique=True, verbose_name='供应商名'),
        ),
        migrations.CreateModel(
            name='PublicAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateField(verbose_name='日期')),
                ('type', models.SmallIntegerField(choices=[(1, '货款'), (2, '报销单'), (3, '专项')], verbose_name='类型')),
                ('product_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='品名')),
                ('product_model', models.CharField(blank=True, max_length=16, null=True, verbose_name='型号')),
                ('unit_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='单价')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='总价')),
                ('tax', models.SmallIntegerField(choices=[(1, '是'), (2, '否')], verbose_name='含税')),
                ('bill', models.CharField(blank=True, max_length=64, null=True, verbose_name='发票备注')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rjd.supplier', to_field='supplier_name')),
            ],
        ),
        migrations.CreateModel(
            name='PrivateAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateField(verbose_name='日期')),
                ('product_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='品名')),
                ('unit_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='单价')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='总价')),
                ('remark', models.CharField(blank=True, max_length=128, null=True, verbose_name='备注')),
                ('img', models.FileField(blank=True, max_length=128, null=True, upload_to='rjd/', verbose_name='图片说明')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rjd.supplier', to_field='supplier_name')),
            ],
        ),
    ]
