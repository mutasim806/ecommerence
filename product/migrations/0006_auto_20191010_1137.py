# Generated by Django 2.2.6 on 2019-10-10 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20191010_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='Images',
            field=models.FileField(upload_to='Images/'),
        ),
    ]
