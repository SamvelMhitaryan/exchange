from rest_framework import serializers
from django.db.models import Sum, F
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from .models import UserCurrency

User = get_user_model()


class CreateUserSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserCurrencySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='currency.id')
    name = serializers.CharField(source='currency.name')

    class Meta:
        model = UserCurrency
        fields = ['id', 'name', 'amount']


class UserSerializer(serializers.ModelSerializer):
    total_currencies_sum = serializers.SerializerMethodField()
    currency = UserCurrencySerializer(many=True, source='user_currency')

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name',
                  'total_currencies_sum', 'currency']

    def get_total_currencies_sum(self, obj):
        total_sum = User.objects.filter(pk=obj.pk).aggregate(
            total=Sum(F('user_currency__amount')
                      * F('currencies__value')))
        result = total_sum['total']
        if result is None:
            return 0
        return result


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password']
