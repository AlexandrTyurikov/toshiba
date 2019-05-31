from django.contrib import admin
from . import models


class CartAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'creation_date',
        'update_date',
    )
    list_filter = ('user',)


class BookInCartAdmin(admin.ModelAdmin):
    list_display = (
        'cart',
        'book',
        'quantity',
        'creation_date',
        'update_date',
    )


admin.site.register(models.Cart, CartAdmin)
admin.site.register(models.BookInCart, BookInCartAdmin)
