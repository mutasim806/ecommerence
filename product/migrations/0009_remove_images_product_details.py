# Generated by Django 2.2.6 on 2019-10-10 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20191010_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='product_details',
        ),
    ]