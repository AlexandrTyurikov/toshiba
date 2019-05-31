from django.urls import path
from .views import BookDetail, BookList, BookCreate, BookUpdate, BookDelete


urlpatterns = [
    path('<int:pk>', BookDetail.as_view(), name='book-detail'),
    path('list/', BookList.as_view(), name='book-list'),
    path('create/', BookCreate.as_view(), name='book-create'),
    path('create/<int:pk>', BookUpdate.as_view(), name='book-update'),
    path('<int:pk>/delete/', BookDelete.as_view(), name='book-delete')
]
