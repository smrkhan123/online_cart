# Generated by Django 2.2.4 on 2019-10-08 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycart', '0019_auto_20191008_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
