from django.contrib import admin
from django.urls import path

from music.models import Artist, Album, Song


admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)

urlpatterns = [
    path('admin/', admin.site.urls),

]


