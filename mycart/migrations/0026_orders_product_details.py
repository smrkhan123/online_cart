# Generated by Django 2.2.4 on 2019-10-08 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycart', '0025_auto_20191009_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='product_details',
            field=models.CharField(default='', max_length=100),
        ),
    ]
