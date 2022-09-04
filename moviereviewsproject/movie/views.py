from re import search
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Movie

# Create your views here.


def home(request):
    searchTerm = request.GET.get('searchMovie')
    movie = Movie.objects.all()
    if searchTerm:
        movie = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movie = Movie.objects.all()
    return render(request, 'home.html', {'name': 'Silver',
                                       'link': 'https://web.flow.opera.com/ext/v1/gx/index-57d9e5df9bd2557f99642f313e2d7f0ed4d96c00d918ee96332b87bb6195c5d0.html',
                                       'searchTerm': searchTerm,
                                       'movies':movie})


def about(request):
    return HttpResponse(" <h1>My initial Page!</h1>")


def siginup(request):
    email = request.GET.get('email')
    return render(request, 'siginup.html', {'email': email})


def detail(request,movie_id):
    movie = get_object_or_404(Movie,pk = movie_id)
    return render (request, 'detail.html', {'movie':movie})