# Python
from typing import Any

# Django
from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from django.shortcuts import render

# Local
<<<<<<< HEAD
from .models import Artist , Song


def base(request):
    songs = Song.objects.all()
    context = {
        'songs': songs
    }
    return render(
        request,
        'main/base.html',
        context
    )

def index(request):
    artists = Artist.objects.all()
    context = {
        'artists': artists
=======
from .models import (
    Album,
    Artist
)


def index(request: WSGIRequest) -> HttpResponse:
    """index."""

    # TODO: сделать так чтобы текущий
    # юзер мог видеть только свои альбомы
    # user: User = request.user
    #
    albums: QuerySet[Album] = Album.objects.all()
    context: dict[str, QuerySet[Any]] = {
        'albums': albums
>>>>>>> f3dc8e05be5e4a1c2beaf3d99f7d653251d522da
    }
    return render(
        request,
        'main/index.html',
        context
<<<<<<< HEAD
    )
=======
    )


def detail(
    request: WSGIRequest,
    album_id: int
) -> HttpResponse:
    """detail."""

    user: User = request.user
    album: QuerySet[Album] = Album.objects.get(
        id=album_id
    )
    context: dict[str, QuerySet[Any]] = {
        'album': album,
        'user': user
    }
    return render(
        request,
        'main/detail.html',
        context
    )
>>>>>>> f3dc8e05be5e4a1c2beaf3d99f7d653251d522da
