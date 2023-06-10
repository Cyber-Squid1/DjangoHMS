from django.urls import path
from HMS.views import *

urlpatterns = [
    path('',Home,name='Home'),
    path('adminLogin/',AdminLogin,name='AdminLogin'),
]
