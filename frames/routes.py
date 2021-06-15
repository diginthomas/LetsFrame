from django.urls import path
from.views import  *

urlpatterns = [
    path('',frameplan),
    path('/<type>',showUserform),
    path('/getdetails',getFormdetails),

]