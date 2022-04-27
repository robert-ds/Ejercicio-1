from django.shortcuts import render
from .models import Movies, Director, Genre
from django.views import generic


def index(request):
    num_movies = Movies.objects.all().count()
    num_directors = Director.objects.all().count()

    return render(
        request,
        'index.html',
        context={
            'num_movies': num_movies,
            'num_directors': num_directors
        }
    )


class MovieListView(generic.ListView):
    model = Movies


class MovieDetailView(generic.DetailView):
    model = Movies
