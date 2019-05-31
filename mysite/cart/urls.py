from django.urls import path
from .views import AddBookToCart, CartView, DeleteFromCart


urlpatterns = [
    path('', CartView.as_view(), name='cart-view'),
    path('<int:pk>', AddBookToCart.as_view(), name='add-to-cart'),
    path('<int:pk>/delete/', DeleteFromCart.as_view(), name='book-in-cart-delete'),
]
