from django.urls import path
from book.views import BookDetail, BookList, BookCreate, BookUpdate, BookDelete


urlpatterns = [
    path('<int:pk>', BookDetail.as_view(), name='book_dv'),
    path('list', BookList.as_view(), name='book_lv'),
    path('create/', BookCreate.as_view(), name='book_cv'),
    path('create/<int:pk>', BookUpdate.as_view(), name='book_uv'),
    path('<int:pk>/delete/', BookDelete.as_view(), name='book_del_v')
]
