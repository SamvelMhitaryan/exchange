from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import UserCurrency


User = get_user_model()

admin.site.register(User, UserAdmin)
admin.site.register(UserCurrency)


class Adminka(admin.ModelAdmin):
    list_display = UserCurrency
    '''переопределить админку так, чтобы заходя на страницу юзера
    было видно сколько у него каких деней'''
