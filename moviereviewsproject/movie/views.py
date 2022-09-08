from cmath import log
from warnings import catch_warnings
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,redirect
from .models import Movie,Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
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
    reviews = Review.objects.filter(movie=movie)
    return render (request, 'detail.html', {'movie':movie,
                                            'reviews':reviews})

@login_required
def createreview(request,movie_id):
    movie = get_object_or_404(Movie,pk=movie_id)
    if request.method == 'GET':
        return render(request,'createreview.html',{
                                            'form':ReviewForm(),
                                            'movie':movie})
    
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.movie = movie
            newReview.save()
            return redirect('detail',newReview.movie.id)
        except ValueError:
            return render(request,
                         'createreview.html',
                         {'form':ReviewForm(),
                         'error':'😑bad Data Passed...😑'})

@login_required
def updatereview(request,review_id):
    review = get_object_or_404(Review, pk=review_id, user = request.user)
    if request.method == 'GET':
        form = ReviewForm(instance = review)
        return render(request,'updatereview.html',{ 'review':review,
                                                    'form':form})
    else:
        try:
            form = ReviewForm(request.POST,instance=review)
            form.save()
            return redirect('detail',review.movie.id)
        except ValueError:
            return render(request,'updatereview.html',{ 'review':review,
                                                        'form':form,
                                                      'error': error})


@login_required
def deletereview(request,review_id):
    review = get_object_or_404(Review,pk = review_id,user = request.user)
    review.delete()
    return redirect('detail',review.movie.id)

