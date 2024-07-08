from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Album(models.Model):
    artist = models.ForeignKey(Artist, related_name='albums', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Song(models.Model):
    album = models.ForeignKey(Album, related_name='song', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    length = models.CharField(max_length=10)

    def __str__(self):
        return self.title
