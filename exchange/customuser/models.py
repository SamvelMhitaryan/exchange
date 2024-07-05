from typing import TYPE_CHECKING

from django.contrib.auth.models import AbstractUser
from django.db import models

if TYPE_CHECKING:
    from currency.models import Cart


class User(AbstractUser):
    currencies = models.ManyToManyField('currency.Currency', related_name='users',
                                        verbose_name='Валюта', through='UserCurrency')
    cart: "Cart"

    def clear_cart(self):
        self.cart.currency.clear()


class UserCurrency(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Пользователь',
        related_name='user_currency')
    currency = models.ForeignKey(
        'currency.Currency', on_delete=models.CASCADE, verbose_name='Валюта',
        related_name='user_currency')
    amount = models.PositiveIntegerField(default=1, verbose_name='Количество')

    class Meta:
        verbose_name = 'Пользователь-валюта'
        verbose_name_plural = 'Пользователи-валюты'

    def __str__(self) -> str:
        return f'{self.user}, {self.currency}, {self.amount}'
