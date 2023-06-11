from HMS.models import *
from django.shortcuts import render,redirect
from django.http import HttpResponseBadRequest
# Create your views here.

def Home(request):
    return render(request, 'index.html')

def AdminLogin(request):
    return render(request,'adminlogin.html')

def DoctorLogin(request):
    return render(request,'doctorlogin.html')

def PatientLogin(request):
    if 'email' in request.session:
        return redirect('PatientDashboard')
    else:
        if request.method=='POST':
            email1=request.POST['email']
            password1=request.POST['password']
            try:
                tempUserData=Patient.objects.get(patientEmail=email1,password=password1)
                if tempUserData:
                    request.session['email']=tempUserData.patientEmail
                    print("Session id:",request.session['email'])
                    return redirect('PatientDashboard')
                else:
                    return render(request,'patientLogin.html',{'message':'Please enter valid credentials.'})
            except:
                return render(request,'patientLogin.html',{"message":'Please enter valid credentials.'})
        return render(request,'patientlogin.html')

def PatientDashboard(request):
    return render(request,'patient_dashboard.html')

def PatientLogout(request):
    if 'email' in request.session.keys():
        del request.session['email']
        return redirect('Home')
    else:
        return redirect('Home')

def AdminSignup(request):
    return render(request,'adminsignup.html')

def DoctorSignup(request):
    return render(request,'doctorsignup.html')

def PatientSignup(request):
    if request.method=="POST":
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        address1=request.POST['address']
        email1=request.POST['email']
        password1=request.POST['password']
        phone1=request.POST['mob']
        check=Patient.objects.filter(patientEmail=email1)
        fullName=fname+" "+lname
        if check:
            return render(request,'patientsignup.html',{'messagesignin':"User already exists with this email"})
        else:
            data=Patient(patientName=fullName,patientEmail=email1,password=password1,phone=phone1,address=address1)
            data.save()
            return redirect('PatientLogin')
    return render(request,'patientsignup.html')

def ContactUs(request):
    if 'email' in request.session:
        if request.method=="GET":
            userData=Patient.objects.get(email=request.session['email'])
            return render(request,'contactus.html',{"userData":userData,"isLoggedIn":1})
        if request.method=="POST":
            name1=request.POST['name']
            phone=request.POST['mob']
            email1=request.POST['email']
            message1=request.POST['feedbackmsg']
            data=Feedback.objects.create(name=name1,email=email1,phonenumber=phone,message=message1)
            return render(request,'contactus.html',{"data":data,"isLoggedIn":1,"message":"Your Query has been recorded"})
        return render(request,'contactus.html',{"data":data,"isLoggedIn":1})
    else:
        if request.method=="POST":
            name1=request.POST['name']
            phone=request.POST['mob']
            email1=request.POST['email']
            message1=request.POST['feedbackmsg']
            data=Feedback.objects.create(name=name1,email=email1,phonenumber=phone,message=message1)
            return render(request,'contactus.html',{"isLoggedIn":0,"message":"Your Query has been recorded"})
        return render(request,'contactus.html',{"isLoggedIn":0})

