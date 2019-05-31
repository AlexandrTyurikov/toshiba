from django.contrib import admin
from . import models


class PublishingAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name',)

#    class Meta:
#        model = models.Publishing


class AuthorAdmin(admin.ModelAdmin):
    list_filter = ('name',)


class GenreAdmin(admin.ModelAdmin):
    list_filter = ('name',)


class SeriesAdmin(admin.ModelAdmin):
    list_filter = ('name',)


admin.site.register(models.Publishing, PublishingAdmin)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Genre, GenreAdmin)
admin.site.register(models.Series, SeriesAdmin)
