# Generated by Django 2.2.4 on 2019-10-01 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycart', '0003_auto_20191001_2336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='gift_choice',
        ),
        migrations.AddField(
            model_name='product',
            name='gift',
            field=models.CharField(choices=[('babygift', 'BABYGIFT'), ('birthdaygift', 'BIRTHDAYGIFT'), ('cristamgift', 'CRISTAMGIFT'), ('accentsgift', 'ACCENTSGIFT'), ('toysgift', 'TOYSGIFT'), ('artificialgift', 'ARTIFICIALGIFT'), ('valentinegift', 'VALENTINEGIFT'), ('giftforher', 'GIFTFORHER'), ('giftforhim', 'GIFTFORHIM')], default='babygift', max_length=15),
        ),
    ]
