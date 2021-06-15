from django.urls import path
from.views import *

urlpatterns = [
      path('',shootsplan),
      path('/getrequest',get_shoots_Req ),


    ]

