from django import forms
from django.forms import ModelForm
from .models import Author, Series, Genre, Publishing


class SearchForm(forms.Form):
    search = forms.CharField(label='Введите ключевое слово', required=False)


class AuthorCrUpForm(ModelForm):
    class Meta:
        model = Author
        fields = (
            'name',
            'description'
        )


class SeriesCrUpForm(ModelForm):
    class Meta:
        model = Series
        fields = (
            'name',
            'description'
        )


class GenreCrUpForm(ModelForm):
    class Meta:
        model = Genre
        fields = (
            'name',
            'description'
        )


class PublishingCrUpForm(ModelForm):
    class Meta:
        model = Publishing
        fields = (
            'name',
            'description'
        )
