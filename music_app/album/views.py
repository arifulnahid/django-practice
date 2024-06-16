from django.shortcuts import render, redirect
from .forms import AlbumForm
from .models import Album

# Create your views here.


def album(request):
    album_form = AlbumForm()
    return render(request, 'album.html', {'form': album_form})


def add_album(request):
    album_form = AlbumForm()
    if request.method == 'POST':
        album_form = AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('album')
    return render(request, 'album.html', {'form': album_form})


def edit_album(request, id):
    try:
        album = Album.objects.get(pk=id)
        album_form = AlbumForm(instance=album)
        if request.method == 'POST':
            album_form = AlbumForm(request.POST, instance=album)
            if album_form.is_valid():
                album_form.save()
                return redirect('album')
        return render(request, 'album.html', {'form': album_form})
    except:
        redirect('album')


def delete_album(request):
    try:
        album = Album.objects.get(pk=id)
        album.delete()
        return redirect('album')
    except:
        return redirect('album')
