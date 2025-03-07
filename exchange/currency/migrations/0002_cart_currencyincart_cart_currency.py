# Generated by Django 5.0 on 2023-12-28 12:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
            },
        ),
        migrations.CreateModel(
            name='CurrencyInCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currency_in_cart', to='currency.cart')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currency_in_cart', to='currency.currency')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='currency',
            field=models.ManyToManyField(related_name='carts', through='currency.CurrencyInCart', to='currency.currency', verbose_name='Валюта'),
        ),
    ]
