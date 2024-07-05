from django.contrib import admin
from django.db.models import QuerySet, F
from .models import *
from customuser.models import UserCurrency


class CurrencyInCartAdmin(admin.ModelAdmin):
    actions = ["confirm_transaction"]

    @admin.action(description="admin confirms the transaction")
    def confirm_transaction(self, request, queryset: QuerySet, *args, **kwargs):
        currencies_in_carts: list[CurrencyInCart] = list(queryset)
        for cur in currencies_in_carts:
            q = UserCurrency.objects.filter(
                user=cur.cart.user, currency=cur.currency)
            if q.exists():
                q.update(
                    amount=F('amount') + cur.amount
                )
            else:
                UserCurrency.objects.create(
                    user=cur.cart.user,
                    currency=cur.currency,
                    amount=cur.amount
                )
            cur.delete()


admin.site.register(Currency)
admin.site.register(Cart)
admin.site.register(CurrencyInCart, CurrencyInCartAdmin)
