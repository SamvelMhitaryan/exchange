from .views import CurrencyView
from django.urls import path


urlpatterns = [
    path('api/currency/', CurrencyView.as_view(),
         name='currency-view'),

]
