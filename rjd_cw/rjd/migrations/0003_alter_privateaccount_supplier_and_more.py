# Generated by Django 4.1.7 on 2023-05-08 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rjd', '0002_alter_supplier_supplier_name_publicaccount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privateaccount',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rjd.supplier'),
        ),
        migrations.AlterField(
            model_name='publicaccount',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rjd.supplier'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='supplier_name',
            field=models.CharField(max_length=32, verbose_name='供应商名'),
        ),
    ]
