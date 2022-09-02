from re import search
from django.shortcuts import render
# from django.http import HttpResponse


# Create your views here.


def home(request):
    searchTerm = request.GET.get('searchMovie')
    return render(request,'home.html',{'name':'Silver',
                                       'link': 'https://web.flow.opera.com/ext/v1/gx/index-57d9e5df9bd2557f99642f313e2d7f0ed4d96c00d918ee96332b87bb6195c5d0.html',
                                       'searchTerm':searchTerm})


def about(request):
    return HttpResponse(" <h1>My initial Page!</h1>")


def siginup(request):
    email = request.GET.get('email')
    return render(request,'siginup.html',{'email':email})
