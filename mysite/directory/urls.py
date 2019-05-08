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
    path('author/<int:pk>', AuthorDetail.as_view(), name='author_dv'),
    path('series/<int:pk>', SeriesDetail.as_view(), name='series_dv'),
    path('genre/<int:pk>', GenreDetail.as_view(), name='genre_dv'),
    path('publishing/<int:pk>', PublishingDetail.as_view(), name='publishing_dv'),

    path('author/', AuthorList.as_view(), name='author_lv'),
    path('series/', SeriesList.as_view(), name='series_lv'),
    path('genre/', GenreList.as_view(), name='genre_lv'),
    path('publishing/', PublishingList.as_view(), name='publishing_lv'),

    path('all_directory/', AllDirectoryView.as_view(), name='all_directory'),

    path('create/author/', AuthorCreate.as_view(), name='author_cv'),
    path('create/series/', SeriesCreate.as_view(), name='series_cv'),
    path('create/genre/', GenreCreate.as_view(), name='genre_cv'),
    path('create/publishing/', PublishingCreate.as_view(), name='publishing_cv'),

    path('update/author/<int:pk>', AuthorUpdate.as_view(), name='author_uv'),
    path('update/series/<int:pk>', SeriesUpdate.as_view(), name='series_uv'),
    path('update/genre/<int:pk>', GenreUpdate.as_view(), name='genre_uv'),
    path('update/publishing/<int:pk>', PublishingUpdate.as_view(), name='publishing_uv'),

    path('author/<int:pk>/delete/', AuthorDelete.as_view(), name='author_del_v'),
    path('series/<int:pk>/delete/', SeriesDelete.as_view(), name='series_del_v'),
    path('genre/<int:pk>/delete/', GenreDelete.as_view(), name='genre_del_v'),
    path('publishing/<int:pk>/delete/', PublishingDelete.as_view(), name='publishing_del_v'),
]
