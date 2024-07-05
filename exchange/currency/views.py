from .serializers import CurrencyModelSerializer, CurrencyModelSerializer
from .models import Currency, CurrencyInCart

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


class CurrencyView(APIView):
    def get(self, request, *args, **kwargs):
        currency = Currency.objects.all()
        return Response(CurrencyModelSerializer(currency, many=True).data)


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencyModelSerializer

    @action(detail=False, methods=['post'])
    def add_to_cart(self, request):
        pk_currency = request.data.get(Currency.pk)
        if not Currency:
            return Response(status=400)
        pk_cart = request.data.get('carts_id')
        amount = request.data.get('amount', 1)
        currencies = get_object_or_404(Currency, pk=pk_currency)

        currency, _ = Currency.objects.get_or_create(pk=pk_cart)

        currency_in_cart = CurrencyInCart.objects.filter(
            currencies=currencies, currency=currency)
        if currency_in_cart:
            currency_in_cart.amount += amount
            currency_in_cart.save()
        else:
            currency_in_cart = CurrencyInCart.objects.create(
                currencies=currencies, currency=currency, amount=amount)

        serializer = CurrencyModelSerializer(currency)
        return Response(serializer.data)
