from django.db import models

# Create your models here.

class GetinTouch(models.Model):
    Name= models.CharField(max_length=25)
    Email=models.EmailField(max_length=254)
    Message=models.TextField()