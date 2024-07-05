from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Currency(models.Model):
    numcode = models.CharField(
        max_length=3, unique=True, db_index=True, verbose_name='Цифровой код')
    charcode = models.CharField(max_length=3, verbose_name='Код валюта')
    nominal = models.IntegerField(verbose_name='Номинальность')
    name = models.CharField(max_length=100,
                            verbose_name='Название')
    value = models.FloatField(verbose_name='Курс')
    vunitrate = models.FloatField(verbose_name='Курс за единицу валюты')

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'

    def __str__(self):
        return self.name


class Cart(models.Model):
    currency = models.ManyToManyField(Currency, related_name='carts',
                                      verbose_name='Валюта', through='CurrencyInCart')
    user = models.OneToOneField('customuser.User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class CurrencyInCart(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE,
                                 related_name='currency_in_cart')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,
                             related_name='currency_in_cart')
    amount = models.PositiveIntegerField(verbose_name='Количество',
                                         default=1)

    def __str__(self):
        return f'Валюта "{self.currency.name}" в корзине {self.cart.pk}'
