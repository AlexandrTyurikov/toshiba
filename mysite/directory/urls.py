from django.urls import path
from directory.views import (
    AllDirectoryView,
    AuthorDetail,
    SeriesDetail,
    GenreDetail,
    PublishingDetail,
    AuthorList,
    SeriesList,
    GenreList,
    PublishingList,
    AuthorCreate,
    SeriesCreate,
    GenreCreate,
    PublishingCreate,
    AuthorUpdate,
    SeriesUpdate,
    GenreUpdate,
    PublishingUpdate,
    AuthorDelete,
    SeriesDelete,
    GenreDelete,
    PublishingDelete
)

urlpatterns = [
    path('author/<int:pk>', AuthorDetail.as_view(), name='author-detail'),
    path('series/<int:pk>', SeriesDetail.as_view(), name='series-detail'),
    path('genre/<int:pk>', GenreDetail.as_view(), name='genre-detail'),
    path('publishing/<int:pk>', PublishingDetail.as_view(), name='publishing-detail'),

    path('author/', AuthorList.as_view(), name='author-list'),
    path('series/', SeriesList.as_view(), name='series-list'),
    path('genre/', GenreList.as_view(), name='genre-list'),
    path('publishing/', PublishingList.as_view(), name='publishing-list'),

    path('all_directory/', AllDirectoryView.as_view(), name='all-directory'),

    path('create/author/', AuthorCreate.as_view(), name='author-create'),
    path('create/series/', SeriesCreate.as_view(), name='series-create'),
    path('create/genre/', GenreCreate.as_view(), name='genre-create'),
    path('create/publishing/', PublishingCreate.as_view(), name='publishing-create'),

    path('update/author/<int:pk>', AuthorUpdate.as_view(), name='author-update'),
    path('update/series/<int:pk>', SeriesUpdate.as_view(), name='series-update'),
    path('update/genre/<int:pk>', GenreUpdate.as_view(), name='genre-update'),
    path('update/publishing/<int:pk>', PublishingUpdate.as_view(), name='publishing-update'),

    path('author/<int:pk>/delete/', AuthorDelete.as_view(), name='author-delete'),
    path('series/<int:pk>/delete/', SeriesDelete.as_view(), name='series-delete'),
    path('genre/<int:pk>/delete/', GenreDelete.as_view(), name='genre-delete'),
    path('publishing/<int:pk>/delete/', PublishingDelete.as_view(), name='publishing-delete'),
]
