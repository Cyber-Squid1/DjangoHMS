from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request, 'index.html')

def AdminLogin(request):
    return render(request,'adminlogin.html')