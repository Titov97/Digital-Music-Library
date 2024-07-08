from django.contrib import admin
from django.urls import path

from music.models import Artist, Album, Song
from music.views import artist, album, song

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)

urlpatterns = [
    path('admin/', admin.site.urls),

]

# Register your models here.
