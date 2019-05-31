from django.contrib import admin
from . import models


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'status',
        'creation_date',
        'update_date'
    )


admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.OrderStatus)
