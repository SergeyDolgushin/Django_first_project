from django.contrib import admin

# Register your models here.
from .models import StockProduct, Stock, Product


@admin.register(StockProduct)
class StockProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'price']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['address', 'id']
