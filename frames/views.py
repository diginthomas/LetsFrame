from django.shortcuts import render


# Create your views here.
def frameplan(request):
    return render(request,'frameplan.html')

def showUserform(requsest,type):
    return render(requsest,'frameForm.html',{'type':type})
def getFormdetails(requsest):
    print(requsest)

