# Generated by Django 2.2.4 on 2019-10-03 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycart', '0010_auto_20191003_1148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='pub_date',
        ),
    ]