# Generated by Django 4.1.7 on 2023-04-11 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sky', '0010_dgdata_dgstatus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dgdata',
            name='work_output',
        ),
        migrations.AddField(
            model_name='dgdata',
            name='efficiency',
            field=models.FloatField(default=0, verbose_name='当前节拍'),
        ),
        migrations.AlterField(
            model_name='dgdata',
            name='total_output',
            field=models.IntegerField(default=0, verbose_name='总产量'),
        ),
    ]
