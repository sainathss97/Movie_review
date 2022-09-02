from distutils.command.upload import upload
from turtle import title
from django.db import models

# Create your models here.

class Movie(models.Model):
    ''' Database for Movies collection '''
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to = 'movie/images/')
    url = models.URLField(blank=True)

    