# Generated by Django 2.0 on 2020-12-23 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_client_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='client_price',
        ),
    ]
