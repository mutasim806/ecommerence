# Generated by Django 2.2.6 on 2019-10-10 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20191009_1942'),
    ]

    operations = [
        migrations.RenameField(
            model_name='capacity',
            old_name='productID',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='description',
            old_name='productID',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='images',
            old_name='productID',
            new_name='product',
        ),
    ]
