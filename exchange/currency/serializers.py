from rest_framework import serializers
from .models import Currency, CurrencyInCart
from django.db.models import Sum


class CurrencyInCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyInCart
        fields = '__all__'


class CurrencyModelSerializer(serializers.ModelSerializer):
    currency_in_carts = CurrencyInCartSerializer(many=True)
    all_currencies_amount = serializers.SerializerMethodField()

    class Meta:
        model = Currency
        fields = '__all__'

    def get_all_currencies_amount(self, obj):
        result = obj.currency_in_cart.aggregate(Sum('amount'))
        return result['amount__sum']
