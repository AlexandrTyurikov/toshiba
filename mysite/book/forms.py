from django import forms
from django.forms import ModelForm
from .models import *


class SearchActiveForm(forms.Form):
    # search = forms.CharField(label='Поиск', required=False)
    active = forms.BooleanField(required=False)


# class SearchForm(forms.Form):
#     search = forms.CharField(label='Введите ключевое слово:', required=False)


class BookCrUpForm(ModelForm):
    class Meta:
        model = Book
        fields = (
            'name',
            'image',
            'price',
            'author',
            'genre',
            'series',
            'publishing',
            'year',
            'pages',
            'binding',
            'format',
            'isbn',
            'weight',
            'age_limit',
            'sum',
            'active',
            'rating'
        )


# class BookUpdateForm(ModelForm):
#     class Meta:
#         model = Book
#         fields = (
#             'name',
#             'image',
#             'price',
#             'author',
#             'genre',
#             'series',
#             'publishing',
#             'year',
#             'pages',
#             'binding',
#             'format',
#             'isbn',
#             'weight',
#             'age_limit',
#             'sum',
#             'active',
#             'rating'
#         )
