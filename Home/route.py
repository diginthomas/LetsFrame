from django.urls import path
from.views import *
urlpatterns = [
    path('',home),
    path ('index',index),
    path('sell',selling),
    path('aboutus',aboutus),
    path ('aboutus/getintouch',getinTouch),


]