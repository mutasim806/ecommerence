# Generated by Django 2.1.11 on 2019-10-08 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='Image',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='images',
            name='Images',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
