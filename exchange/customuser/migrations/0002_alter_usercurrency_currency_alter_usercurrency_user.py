# Generated by Django 5.0 on 2023-12-27 09:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
        ('customuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercurrency',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_currency', to='currency.currency', verbose_name='Валюта'),
        ),
        migrations.AlterField(
            model_name='usercurrency',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_currency', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
