from django.db import models

class Poster(models.Model):
    PosterName=models.CharField(max_length=50)
    PosterDesc=models.TextField()
    PosterPrice=models.CharField( max_length=10)
    PosterSize=models.CharField(max_length=10)
    PosterImageURL=models.TextField()

