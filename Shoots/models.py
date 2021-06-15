from django.db import models

# Create your models here.
class ShootsReq(models.Model):
    Name = models.CharField(max_length=25)
    Email = models.EmailField(max_length=254)
    Phonenumber = models.CharField(max_length=10)
    Pincode     = models.CharField(max_length=6)
    Address = models.TextField()