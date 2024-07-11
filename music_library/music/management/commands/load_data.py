import json
from django.core.management.base import BaseCommand
from music.models import Artist, Album, Song


class Command(BaseCommand):
    help = 'Load data from data.json into the database'

    def handle(self, *args, **kwargs):
        with open('data.json') as f:
            data = json.load(f)
            for artist_data in data:
                artist, created = Artist.objects.get_or_create(name=artist_data['name'])
                for album_data in artist_data['albums']:
                    album, created = Album.objects.get_or_create(
                        artist=artist,
                        title=album_data['title'],
                        defaults={'description': album_data['description']}
                    )
                    for song_data in album_data['songs']:
                        Song.objects.get_or_create(
                            album=album,
                            title=song_data['title'],
                            defaults={'length': song_data['length']}
                        )
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
