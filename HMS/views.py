from HMS.models import *
from django.shortcuts import render,redirect
from django.http import HttpResponseBadRequest
import datetime
# Create your views here.

def Home(request):
    return render(request, 'index.html')

def AdminLogin(request):
    return render(request,'adminlogin.html')

def DoctorLogin(request):
    if 'doctorEmail' in request.session:
        return redirect('DoctorDashboard')
    else:
        if request.method=='POST':
            email1=request.POST['email']
            password1=request.POST['password']
            try:
                tempData=Doctor.objects.get(doctorEmail=email1,password=password1)
                if tempData:
                    request.session['doctorEmail']=tempData.doctorEmail
                    print("Session id:",request.session['doctorEmail'])
                    return redirect('DoctorDashboard')
                else:
                    return render(request,'doctorLogin.html',{'message':'Please enter valid credentials.'})
            except:
                return render(request,'doctorLogin.html',{"message":'Please enter valid credentials.'})
        return render(request,'doctorLogin.html')

def DoctorDashboard(request):
    if 'doctorEmail' in request.session:
        return render(request,'doctor_dashboard.html')

def ViewPatientRecords(request):
    if 'doctorEmail' in request.session:
        myData=Doctor.objects.get(doctorEmail=request.session['doctorEmail'])
        docId=myData.pk
        tempPatientAppoinmentData=Appointment.objects.filter(doctorId=docId)
        patientList=[]
        for i in tempPatientAppoinmentData:
            patientDict={}
            tempPatientData=Patient.objects.get(id=i.patientId)
            patientDict['name']=tempPatientData.patientName
            patientDict['phone']=tempPatientData.phone
            patientDict['address']=tempPatientData.address
            patientDict['symptoms']=tempPatientData.symptoms
            patientDict['medicines']=i.medicinePrescribed
            patientDict['description']=i.description
            patientList.append(patientDict)
        return render(request,'doctor_view_patient.html',{"patientList":patientList})
    else:
        return redirect('DoctorLogin')

def DoctorPatient(request):
    if 'doctorEmail' in request.session:
        return render(request,'doctor_patient.html')

def PatientLogin(request):
    if 'patientEmail' in request.session:
        return redirect('PatientDashboard')
    else:
        if request.method=='POST':
            email1=request.POST['email']
            password1=request.POST['password']
            try:
                tempUserData=Patient.objects.get(patientEmail=email1,password=password1)
                if tempUserData:
                    request.session['patientEmail']=tempUserData.patientEmail
                    print("Session id:",request.session['patientEmail'])
                    return redirect('PatientDashboard')
                else:
                    return render(request,'patientLogin.html',{'message':'Please enter valid credentials.'})
            except:
                return render(request,'patientLogin.html',{"message":'Please enter valid credentials.'})
        return render(request,'patientlogin.html')

def PatientDashboard(request):
    if 'patientEmail' in request.session:
        patientData=Patient.objects.get(patientEmail=request.session['patientEmail'])
        if patientData.currentlyAssignedDoctorId:
            doctorData=Doctor.objects.get(pk=patientData.currentlyAssignedDoctorId)
            return render(request,'patient_dashboard.html',{"hasDoctorAssigned":1,"doctorData":doctorData})
        else:
            return render(request,'patient_dashboard.html',{"hasDoctorAssigned":0})
    # return render(request,'patient_dashboard.html')

def PatientBookAppointment(request):
    if 'patientEmail' in request.session:
        SpecializationList = Specialization.objects.all()
        return render(request,'patient_book_appointment.html',{"SpecializationList":SpecializationList})
    return redirect ('PatientLogin')

def ConfirmAppointment(request):
    if 'patientEmail' in request.session:
        patientData=Patient.objects.get(patientEmail=request.session['patientEmail'])
        pid=patientData.pk
        tempAppointment=Appointment(patientId=pid,doctorId=request.session['SpecialistDoctorId'],description="",medicinePrescribed="",appointmentCost=800,wasAdmitted=False)
        tempAppointment.save()
        Patient.objects.filter(patientEmail=request.session['patientEmail']).update(currentlyAssignedDoctorId=request.session['SpecialistDoctorId'])
        del request.session['SpecialistId']
        del request.session['SpecialistDoctorId']
        return render(request,'patient_appointment.html')

def ShowDoctors(request,doctorSpecialization):
    if 'patientEmail' in request.session:
        SpecializationList = Specialization.objects.all()
        SpecializedDoctorList=Doctor.objects.filter(specialization_id=doctorSpecialization)
        SpecialistSelected=Specialization.objects.get(id=doctorSpecialization)
        request.session['SpecialistId']=doctorSpecialization
        print(request.session['SpecialistId'])
        return render(request,'patient_book_appointment.html',{"SpecializationList":SpecializationList,"SpecializedDoctorList":SpecializedDoctorList,"SpecialistSelected":SpecialistSelected})
    return redirect ('PatientLogin')

def SelectDoctor(request,doctorSpecialization,doctorId):
    if 'patientEmail' in request.session:
        SpecializationList = Specialization.objects.all()
        SpecializedDoctorList=Doctor.objects.filter(specialization_id=doctorSpecialization)
        SpecialistSelected=Specialization.objects.get(id=doctorSpecialization)
        SpecialistDoctorName=Doctor.objects.get(specialization_id=doctorSpecialization,id=doctorId)
        request.session['SpecialistDoctorId']=doctorId
        print(request.session['SpecialistDoctorId'])
        return render(request,'patient_book_appointment.html',{"SpecializationList":SpecializationList,"SpecializedDoctorList":SpecializedDoctorList,"SpecialistSelected":SpecialistSelected,"SpecialistDoctorName":SpecialistDoctorName})


def PatientViewAppointment(request):
    return render(request,'patient_appointment.html')

def Logout(request):
    if 'patientEmail' in request.session.keys():
        del request.session['patientEmail']
        return redirect('Home')
    elif 'doctorEmail' in request.session.keys():
        del request.session['doctorEmail']
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
    if 'patientEmail' in request.session:
        if request.method=="GET":
            userData=Patient.objects.get(email=request.session['patientEmail'])
            return render(request,'contactus.html',{"userData":userData,"isLoggedIn":1})
        if request.method=="POST":
            name1=request.POST['name']
            phone=request.POST['mob']
            email1=request.POST['patientEmail']
            message1=request.POST['feedbackmsg']
            data=Feedback.objects.create(name=name1,email=email1,phonenumber=phone,message=message1)
            return render(request,'contactus.html',{"data":data,"isLoggedIn":1,"message":"Your Query has been recorded"})
        return render(request,'contactus.html',{"data":data,"isLoggedIn":1})
    else:
        if request.method=="POST":
            name1=request.POST['name']
            phone=request.POST['mob']
            email1=request.POST['patientEmail']
            message1=request.POST['feedbackmsg']
            data=Feedback.objects.create(name=name1,email=email1,phonenumber=phone,message=message1)
            return render(request,'contactus.html',{"isLoggedIn":0,"message":"Your Query has been recorded"})
        return render(request,'contactus.html',{"isLoggedIn":0})
