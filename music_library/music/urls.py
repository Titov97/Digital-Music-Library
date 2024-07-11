from django.urls import path
from . import views

urlpatterns = [
    path('', views.artist_list, name='artist_list'),
    path('artist/create/', views.artist_create, name='artist_create'),
    path('artist/<int:artist_id>/', views.artist_detail, name='artist_detail'),
    path('artist/<int:artist_id>/update/', views.artist_update, name='artist_update'),
    path('artist/<int:artist_id>/delete/', views.artist_delete, name='artist_delete'),
    path('album/create/', views.album_create, name='album_create'),
    path('album/create/<int:artist_id>/', views.album_create, name='album_create_for_artist'),
    path('album/<int:album_id>/', views.album_detail, name='album_detail'),
    path('album/<int:album_id>/update/', views.album_update, name='album_update'),
    path('album/<int:album_id>/delete/', views.album_delete, name='album_delete'),
    path('search-artists/', views.search_artists, name='search_artists'),
]
