# Generated by Django 5.0 on 2023-12-27 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
        ('customuser', '0002_alter_usercurrency_currency_alter_usercurrency_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='сurrencies',
            field=models.ManyToManyField(related_name='users', through='customuser.UserCurrency', to='currency.currency', verbose_name='Валюта'),
        ),
    ]
