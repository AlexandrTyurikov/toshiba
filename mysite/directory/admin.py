from django.contrib import admin
from . import models


class PublishingAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

#    class Meta:
#        model = models.Publishing


admin.site.register(models.Publishing, PublishingAdmin)
admin.site.register(models.Author)
admin.site.register(models.Genre)
admin.site.register(models.Series)
