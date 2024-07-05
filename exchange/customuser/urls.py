
from .views import UserGetView
from django.urls import path

urlpatterns = [
    path('me', UserGetView.as_view())
]
