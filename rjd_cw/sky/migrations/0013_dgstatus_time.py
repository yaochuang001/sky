# Generated by Django 4.1.7 on 2023-04-12 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sky', '0012_remove_dgstatus_time_dgstatus_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='dgstatus',
            name='time',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='时间'),
        ),
    ]
