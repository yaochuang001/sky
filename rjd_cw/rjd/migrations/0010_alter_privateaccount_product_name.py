# Generated by Django 4.1.7 on 2023-05-11 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rjd', '0009_alter_privateaccount_supplier_alter_unpaid_supplier_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privateaccount',
            name='product_name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='品名'),
        ),
    ]
