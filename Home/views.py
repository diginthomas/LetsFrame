from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import GetinTouch
def home(request):
    return render(request,'index.html')

def index(request):
    return render(request,'aboutus.html')

def selling(request):
    return render(request,'sellingframes.html')

def aboutus(request):
    return render(request,'moreinfo.html')

def getinTouch(req):
    getinTouch=GetinTouch()
    getinTouch.Name=req.POST['name']
    getinTouch.Email=req.POST['email']
    getinTouch.Message=req.POST['message']
    getinTouch.save()
    return redirect('/')

def showallsubscribers(request):
    getinTouch= GetinTouch.objects.all()
    return render(request,'adminsubscribers.html',{'getintouch':getinTouch})



def adminhome(request):
    return render(request,'adminhome.html')

def price(request):
    return render(request, 'pricing.html')


def login(request):
     return render(request,'login.html')   