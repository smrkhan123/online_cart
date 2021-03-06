# Generated by Django 2.2.4 on 2019-10-03 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycart', '0009_auto_20191003_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Image',
            field=models.ImageField(null=True, upload_to='shop/images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
