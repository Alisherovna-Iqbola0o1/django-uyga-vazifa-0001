from django.contrib import admin
from .models import Savatcha, Buyurtma
# Register your models here.


@admin.register(Savatcha)
class SvatchaAdmin(admin.ModelAdmin):
    list_display = ['user', 'telefon', 'amount', 'created_at']
    search_fields = ['user__name', 'telefon__name']


@admin.register(Buyurtma)
class BuyurtmAdmin(admin.ModelAdmin):
    list_display = ['user', 'addres', 'telefon_raqam', 'jami_narx', 'created_at']
    search_fields = ['user__name', 'telefon_raqam', 'addres']
