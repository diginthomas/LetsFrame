from django.shortcuts import render
from.models import Poster

def showposters(request):
     poster =Poster.objects.all()
     return render(request,'poster.html',{'poster':poster})
    