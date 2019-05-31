from django.contrib import admin
from . import models


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'creation_date',
        'update_date',
    )
    list_filter = ('name',)

#    class Meta:
#        model = models.Book


admin.site.register(models.Book, BookAdmin)
