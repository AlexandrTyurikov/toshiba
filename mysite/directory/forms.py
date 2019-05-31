from django import forms
from .models import Author, Series, Genre, Publishing


class SearchForm(forms.Form):
    search = forms.CharField(label='Введите ключевое слово', required=False)


class AuthorCrUpForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = (
            'name',
            'description'
        )


class SeriesCrUpForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = (
            'name',
            'description'
        )


class GenreCrUpForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = (
            'name',
            'description'
        )


class PublishingCrUpForm(forms.ModelForm):
    class Meta:
        model = Publishing
        fields = (
            'name',
            'description'
        )
