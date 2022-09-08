from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Movie(models.Model):
    ''' Database for Movies collection '''
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to = 'movie/images/')
    url = models.URLField(blank=True)

    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    '''Database for Reviews Model'''
    text = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    movie= models.ForeignKey(Movie,on_delete=models.CASCADE)
    watchAgain = models.BooleanField()

    def __str__(self) -> str:
        return f'{user}->{movie}------\
            {text}'