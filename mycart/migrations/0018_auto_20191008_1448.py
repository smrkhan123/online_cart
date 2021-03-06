# Generated by Django 2.2.4 on 2019-10-08 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycart', '0017_auto_20191005_2327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, null=True)),
                ('desc', models.CharField(max_length=1000, null=True)),
                ('category', models.CharField(max_length=100)),
                ('subcategory', models.CharField(max_length=100, null=True)),
                ('price', models.IntegerField(null=True)),
                ('Image', models.ImageField(null=True, upload_to='shop/images')),
                ('pub_date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('babygift', 'BABYGIFT'), ('birthdaygift', 'BIRTHDAYGIFT'), ('accentsgift', 'ACCENTSGIFT'), ('cristamgift', 'CRISTAMGIFT'), ('toysgift', 'TOYSGIFT'), ('valentinegift', 'VALENTINEGIFT'), ('artificialgift', 'ARTIFICIALGIFT'), ('giftforher', 'GIFTFORHER'), ('giftforhim', 'GIFTFORHIM')], max_length=100),
        ),
    ]
