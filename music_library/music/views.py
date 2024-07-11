from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Artist, Album
from .forms import ArtistForm, AlbumForm


def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'music/artist_list.html', {'artists': artists})


def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    return render(request, 'music/artist_detail.html', {'artist': artist})


def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    return render(request, 'music/album_detail.html', {'album': album})


def search_artists(request):
    query = request.GET.get('q', '')
    if query:
        artists = Artist.objects.filter(name__icontains=query).values('id', 'name')
        return JsonResponse(list(artists), safe=False)
    else:
        artists = Artist.objects.all()
        return render(request, 'music/artist_list.html', {'artists': artists})


# CRUD operations for Artist
def artist_create(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artist_list')
    else:
        form = ArtistForm()
    return render(request, 'music/artist_form.html', {'form': form})


def artist_update(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    if request.method == 'POST':
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('artist_detail', artist_id=artist.id)
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'music/artist_form.html', {'form': form})


def artist_delete(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    if request.method == 'POST':
        artist.delete()
        return redirect('artist_list')
    return render(request, 'music/artist_confirm_delete.html', {'artist': artist})


# CRUD operations for Album
def album_create(request, artist_id=None):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artist_detail', artist_id=form.cleaned_data['artist'].id)
    else:
        form = AlbumForm(initial={'artist': artist_id})
    return render(request, 'music/album_form.html', {'form': form})


def album_update(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_detail', album_id=album.id)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'music/album_form.html', {'form': form})


def album_delete(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    if request.method == 'POST':
        album.delete()
        return redirect('artist_detail', artist_id=album.artist.id)
    return render(request, 'music/album_confirm_delete.html', {'album': album})
