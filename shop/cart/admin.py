from django.contrib import admin

from .models import CartProduct


@admin.register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'buyer']
