# Generated by Django 4.1.7 on 2023-03-08 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cw', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='create_time',
            field=models.DateField(verbose_name='入职时间'),
        ),
    ]
