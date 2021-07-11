from django.shortcuts import render,redirect
from .models import ShootsReq

def shootsplan(request):
    return render(request,'shootsplan.html')

def get_shoots_Req(request):
     shoot= ShootsReq()
     shoot.Name=request.POST['customerName']
     shoot.Email=request.POST['customerEmail']
     shoot.Pincode=request.POST['pincode']
     shoot.Address=request.POST['address']
     shoot.Phonenumber=request.POST['customerPhone']
     shoot.save()
     return redirect('/')


def showreq(request):
    shoot= ShootsReq.objects.all()
    return render(request,'adminreq.html',{'shoot':shoot})
