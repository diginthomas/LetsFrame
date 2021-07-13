from django.urls import path
from.views import *
urlpatterns = [
    path('',home),
    path ('index',index),
    path('sell',selling),
    path('aboutus',aboutus),
    path ('aboutus/getintouch',getinTouch),
    path('adminhome',adminhome),
    path('pricing',price),
    path('admin/showsub',showallsubscribers),
    path('login',login),

]