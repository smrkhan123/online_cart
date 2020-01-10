# Generated by Django 2.2.4 on 2019-10-01 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(choices=[('green', 'GREEN'), ('blue', 'BLUE'), ('red', 'RED'), ('orange', 'ORANGE'), ('black', 'BLACK')], default='green', max_length=6),
        ),
    ]
