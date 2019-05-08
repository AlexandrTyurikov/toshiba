from django.urls import path
from .views import BookCard


urlpatterns = [
    path('', BookCard.as_view(), name='main')
]


