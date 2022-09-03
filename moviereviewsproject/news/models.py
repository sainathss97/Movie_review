from django.db import models

# Create your models here.
class News(models.Model):
    ''' The Database for news '''
    headline = models.CharField(max_length=256)
    body = models.TextField()
    date = models.DateField()