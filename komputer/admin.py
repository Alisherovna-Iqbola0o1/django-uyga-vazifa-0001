from django.contrib import admin
from .models import Komputer

@admin.register(Komputer)
class KomputerAdmin(admin.ModelAdmin):
    list_display = ('name', 'brend', 'price', 'stock', 'xotira', 'ram', 'ekran_olchami', 'created_at')
    search_fields = ('name', 'brend', 'xotira', 'ram', 'ekran_olchami')
