from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def boolparser(value):
    if value == True:
        return mark_safe('<p class="text-success"><i class="fas fa-check-circle"></i></p>')
    elif value != True:
        return mark_safe('<p class="text-danger"><i class="fas fa-times-circle"></i></p>')
    return value


@register.filter
def none(value):
    if value == None:
        return mark_safe('<i class="far fa-circle"></i>')
    return value
