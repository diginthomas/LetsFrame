from django.db import models


# Create your models here.
class FrameOrders(models.Model):
    Name = models.CharField(max_length=25)
    Address = models.TextField()
    Phonenumber = models.CharField(max_length=10)
    Email = models.EmailField(max_length=254)
    Image = models.ImageField(upload_to="framesimages")
    Size =  models.CharField(max_length=6)
    Width = models.IntegerField()
    Price = models.IntegerField()
