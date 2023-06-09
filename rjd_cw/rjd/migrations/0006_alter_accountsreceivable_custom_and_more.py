# Generated by Django 4.1.7 on 2023-05-10 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rjd', '0005_unpaid_accountsreceivable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountsreceivable',
            name='custom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rjd.custominfo', to_field='company_name'),
        ),
        migrations.AlterField(
            model_name='custominfo',
            name='company_name',
            field=models.CharField(max_length=32, unique=True, verbose_name='公司名称'),
        ),
    ]
