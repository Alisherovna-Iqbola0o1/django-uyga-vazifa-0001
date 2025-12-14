from django.contrib import admin
from .models import Telefon
# Register your models here.

@admin.register(Telefon)

class TelefonAdmin(admin.ModelAdmin):
    list_display = ['name', 'brend', 'price', 'image', 'desc', 'stock', 'xotira', 'ram', 'created_at', 'updated_at']
    search_field = ['name', 'brend', 'xotira', 'ram']

