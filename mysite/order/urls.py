from django.urls import path
from .views import OrderCheckoutView, OrderList, OrderDelete, OrderUpdate


urlpatterns = [
    path('', OrderCheckoutView.as_view(), name='order-create'),
    path('<int:pk>', OrderList.as_view(), name='order-list'),
    path('<int:pk>/delete/', OrderDelete.as_view(), name='order-delete'),
    path('update/<int:pk>/', OrderUpdate.as_view(), name='order-update')
]
