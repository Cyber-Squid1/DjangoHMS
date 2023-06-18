from HMS.models import *
from django.shortcuts import render,redirect
from django.http import HttpResponseBadRequest
from datetime import date
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
        doctorData=Doctor.objects.get(doctorEmail=request.session['doctorEmail'])
        # todayDate=datetime.date()
        # AppointmentData=Appointment.objects.filter(appointmentDate=todayDate,status="PENDING") {"appointmentData":AppointmentData}
        return render(request,'doctor_dashboard.html',{"doctorData":doctorData})

def ViewYourPatientRecords(request):
    if 'doctorEmail' in request.session:
        myData=Doctor.objects.get(doctorEmail=request.session['doctorEmail'])
        docId=myData.pk
        patientAppoinmentData=Appointment.objects.filter(doctorId=docId)
        patientList=[]
        idList=[]
        for i in patientAppoinmentData:
            patientDict={}
            patientData=Patient.objects.get(id=i.patientId)
            if i.patientId in idList:
                continue
            else:
                patientDict['pk']=patientData.pk
                patientDict['patientName']=patientData.patientName
                patientDict['phone']=patientData.phone
                patientDict['address']=patientData.address
                idList.append(i.patientId)
                patientList.append(patientDict)
        print("ID list: ",idList)
        return render(request,'doctor_view_patient.html',{"patientList":patientList,"x":2})
    else:
        return redirect('DoctorLogin')

def ViewAllPatientRecords(request):
    if 'doctorEmail' in request.session:
        allPatientsData=Patient.objects.all()
    return render(request,'doctor_view_patient.html',{"patientList":allPatientsData,"x":1})

def ViewSinglePatientRecord(request,patientId,x):
    if 'doctorEmail' in request.session:
        docData=Doctor.objects.get(doctorEmail=request.session['doctorEmail'])
        allRecords=Appointment.objects.filter(patientId=patientId)
        patientRecord=Appointment.objects.filter(patientId=patientId,status="COMPLETED")
        try:
            currentAppointmentData=Appointment.objects.get(patientId=patientId,doctorId=docData.pk,status="PENDING")
        except:
            print()
        patientData=Patient.objects.get(id=patientId)
        if x == 0:
            return render(request,'doctor_view_patient_record.html',{"patientPreviousRecord":patientRecord,"patientData":patientData,"currentAppointmentId":currentAppointmentData.pk,"allRecords":allRecords,"pageChoice":x})
        else:
            return render(request,'doctor_view_patient_record.html',{"patientPreviousRecord":patientRecord,"patientData":patientData,"allRecords":allRecords,"pageChoice":x})

def AppointmentComplete(request,patientId):
    if 'doctorEmail' in request.session:
        symptoms1=request.POST['sym']
        medicine=request.POST['med']
        description1=request.POST['desc']
        currPK=request.POST['currappPK']
        wasAdmitted1=request.POST['wasAdmitted']
        Appointment.objects.filter(id=currPK,patientId=patientId,status="PENDING").update(description=description1,medicinePrescribed=medicine,symptoms=symptoms1,status="COMPLETED",wasAdmitted=bool(wasAdmitted1))
        if bool(wasAdmitted1):
            patientData=Patient.objects.get(id=patientId)
            doctorData=Doctor.objects.get(doctorEmail=request.session['doctorEmail'])
            appointmentData=Appointment.objects.get(id=currPK)
            temp=AdmittedPatientDetails(doctorId=doctorData.pk,patientId=patientData.pk,admittedOn=appointmentData.appointmentDate,appointmentDetailsId=currPK)
            print("Doctorid",doctorData.pk)
            temp.save()
            return render(request,'doctor_admit_patient.html',{"appointmentDetails":appointmentData,"patientData":patientData,"doctorData":doctorData})
        else:
            Patient.objects.filter(id=patientId).update(currentlyAssignedDoctorId="")
            return redirect('DoctorViewAppointment')
    else:
        return redirect('DoctorLogin')

def DoctorViewAppointment(request):
    if 'doctorEmail' in request.session:
        doctorData=Doctor.objects.get(doctorEmail=request.session['doctorEmail'])
        AppointmentData=Appointment.objects.filter(doctorId=doctorData.pk,status="PENDING")
        patientList=[]
        for i in AppointmentData:
            patientData=Patient.objects.get(id=i.patientId)
            patientDict={}
            patientDict['name']=patientData.patientName
            patientDict['phone']=patientData.phone
            patientDict['time']=i.appointmentTime
            patientDict['patientId']=i.patientId
            patientList.append(patientDict)
        return render(request,'doctor_view_appointment.html',{"patientList":patientList,"x":0})

def DoctorPatient(request):
    if 'doctorEmail' in request.session:
        return render(request,'doctor_patient.html')

def ViewAllAdmittedPatients(request):
    if 'doctorEmail' in request.session:
        doctorData=Doctor.objects.get(doctorEmail=request.session['doctorEmail'])
        admittedPatientsData=AdmittedPatientDetails.objects.filter(doctorId=doctorData.pk,status="ADMITTED")
        patientList=[]
        for i in admittedPatientsData:
            patientDict={}
            patientData=Patient.objects.get(id=i.patientId)
            patientDict['patientName']=patientData.patientName
            patientDict['phone']=patientData.phone
            patientDict['address']=patientData.address
            patientDict['admittedOn']=i.admittedOn
            patientDict['appointmentId']=i.appointmentDetailsId
            patientList.append(patientDict)
        return render(request,'doctor_view_admitted_patients.html',{"admittedPatientsData":patientList})
    else:
        return redirect('DoctorLogin')

def ViewAdmittedPatientDetails(request,appointmentId):
    if 'doctorEmail' in request.session:
        print("appointment id",appointmentId)
        admittedPatientDataCurrent=AdmittedPatientDetails.objects.get(appointmentDetailsId=appointmentId)
        appointmentDataCurrent=Appointment.objects.get(id=appointmentId)
        patientData=Patient.objects.get(id=admittedPatientDataCurrent.patientId)
        admittedPatientDataHistory=AdmittedPatientDetails.objects.filter(patientId=patientData.pk,status="DISCHARGED")
        admittedPatientHistory=[]
        for i in admittedPatientDataHistory:
            historyDict={}
            appointmentData=Appointment.objects.get(id=i.appointmentDetailsId)
            historyDict['appointmentDate']=appointmentData.appointmentDate
            historyDict['symptoms']=appointmentData.symptoms
            historyDict['medicine']=appointmentData.medicinePrescribed
            historyDict['description']=appointmentData.description
            historyDict['dischargeDate']=i.dischargeDate
            historyDict['totalCost']=i.totalCost
            admittedPatientHistory.append(historyDict)
        return render(request,'view_admitted_patient_details.html',{"currentData":appointmentDataCurrent,"patientData":patientData,"historyData":admittedPatientHistory})

def UpdateDischargePatient(request):
    if 'doctorEmail' in request.session:
        appointmentId=request.POST['currAppId']
        doctorChoice=request.POST['submitBtn']
        symptoms=request.POST['sym']
        medicine=request.POST['med']
        description=request.POST['desc']
        print(1)
        if doctorChoice == "UPADTE_DETAILS":
            Appointment.objects.filter(id=appointmentId).update(symptoms=symptoms,medicinePrescribed=medicine,description=description)
            return redirect('ViewAllAdmittedPatients')
        elif doctorChoice == "DISCHARGE_PATIENT":
            print("elif")
            roomCharges1=int(1200)
            medicineCost1=int(500)
            otherCost1=int(300)
            totalCost1=roomCharges1+medicineCost1+otherCost1
            print("elif 1")
            dischargeDate1=date.today()
            print('elif 2')
            Appointment.objects.filter(id=appointmentId).update(symptoms=symptoms,medicinePrescribed=medicine,description=description)
            print('elif 3')
            try:
                AdmittedPatientDetails.objects.filter(appointmentDetailsId=appointmentId).update(roomCharges=roomCharges1,MedicineCost=medicineCost1,otherCharges=otherCost1,totalCost=totalCost1,dischargeDate=dischargeDate1,status="DISCHARGED")
                print('try')
            except:
                print("except")
            print('elif 4')
            return redirect('ViewAllAdmittedPatients')

def PatientProfile(request):
    if 'patientEmail' in request.session:
        patientData=Patient.objects.get(patientEmail=request.session['patientEmail'])
        nameList=patientData.patientName.split(' ')
        if request.method=="POST":
            fname=request.POST['firstname']
            lname=request.POST['lastname']
            phone=request.POST['phonenumber']
            address1=request.POST['address']
            fullName=str(fname)+" "+str(lname)
            Patient.objects.filter(patientEmail=request.session['patientEmail']).update(patientName=fullName,phone=phone,address=address1)
            return redirect('PatientProfile')
        print(nameList)
        return render(request,'patient_profile.html',{"patientData":patientData,"firstName":nameList[0],"lastName":nameList[1],"patientName":nameList[0]+nameList[1]})
    else:
        return redirect('PatientLogin')

def PatientMedicalHistory(request):
    return render(request,'patient_view_medical_history.html')

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
            AppointmentData=Appointment.objects.get(patientId=patientData.pk,doctorId=patientData.currentlyAssignedDoctorId,status="PENDING")
            return render(request,'patient_dashboard.html',{"hasDoctorAssigned":1,"doctorData":doctorData,"patientName":patientData.patientName,"appointmentData":AppointmentData})
        else:
            return render(request,'patient_dashboard.html',{"hasDoctorAssigned":0})
    else:
        return redirect('PatientLogin')

def ConfirmAppointment(request):
    if 'patientEmail' in request.session:
        SpecializationList = Specialization.objects.all()
        if 'SpecialistId' and 'SpecialistDoctorId' and 'AppointmentTime' in request.session:
            patientData=Patient.objects.get(patientEmail=request.session['patientEmail'])
            pid=patientData.pk
            tempAppointment=Appointment(patientId=pid,doctorId=request.session['SpecialistDoctorId'],description="",medicinePrescribed="",appointmentCost=800,wasAdmitted=False,appointmentTime=request.session['AppointmentTime'])
            tempAppointment.save()
            Patient.objects.filter(patientEmail=request.session['patientEmail']).update(currentlyAssignedDoctorId=request.session['SpecialistDoctorId'])
            del request.session['SpecialistId']
            del request.session['SpecialistDoctorId']
            return render(request,'patient_appointment.html',{"message":"Appointment booked successfully"})
        else:
            return render(request,'patient_book_appointment.html',{"message":"Please select all the doctor and timing details.","SpecializationList":SpecializationList})
    else:
        return redirect('PatientLogin')

def PatientBookAppointment(request):
    if 'patientEmail' in request.session:
        SpecializationList = Specialization.objects.all()
        return render(request,'patient_book_appointment.html',{"SpecializationList":SpecializationList})
    return redirect ('PatientLogin')

def ShowDoctors(request,doctorSpecialization):
    if 'patientEmail' in request.session:
        SpecializationList = Specialization.objects.all()
        SpecializedDoctorList=Doctor.objects.filter(specialization_id=doctorSpecialization)
        SpecialistSelected=Specialization.objects.get(id=doctorSpecialization)
        request.session['SpecialistId']=doctorSpecialization
        return render(request,'patient_book_appointment.html',{"SpecializationList":SpecializationList,"SpecializedDoctorList":SpecializedDoctorList,"SpecialistSelected":SpecialistSelected})
    return redirect ('PatientLogin')

def SelectDoctor(request,doctorSpecialization,doctorId):
    if 'patientEmail' in request.session:
        if 'SpecialistId' in request.session:
            SpecializationList = Specialization.objects.all()
            SpecializedDoctorList=Doctor.objects.filter(specialization_id=doctorSpecialization)
            SpecialistSelected=Specialization.objects.get(id=doctorSpecialization)
            SpecialistDoctorName=Doctor.objects.get(specialization_id=doctorSpecialization,id=doctorId)
            request.session['SpecialistDoctorId']=doctorId
            
            AppointmentTime=["10:00:00","10:30:00","11:00:00","11:30:00","12:00:00","13:30:00","15:00:00","15:30:00","16:00:00","16:30:00","17:00:00","17:30:00","18:00:00","18:30:00"]
            appointmentData=Appointment.objects.filter(doctorId=doctorId,status="Pending")
            for i in appointmentData:
                if i.appointmentTime in AppointmentTime:
                    AppointmentTime.remove(i.appointmentTime)
            
            return render(request,'patient_book_appointment.html',{"SpecializationList":SpecializationList, "SpecializedDoctorList":SpecializedDoctorList,"SpecialistSelected":SpecialistSelected,"SpecialistDoctorName":SpecialistDoctorName,"AppointmentTime":AppointmentTime})
        else:
            return render(request,'patient_book_appointment.html',{"message":"Please select the specialist you want to book an appointment with.","SpecializationList":SpecializationList})
    else:
        return redirect('PatientLogin')

def SelectTime(request,appointmentTime):
    if 'patientEmail' in request.session:
        SpecializationList = Specialization.objects.all()
        if 'SpecialistId' and 'SpecialistDoctorId' in request.session:
            SpecializedDoctorList=Doctor.objects.filter(specialization_id=request.session['SpecialistId'])
            SpecialistSelected=Specialization.objects.get(id=request.session['SpecialistId'])
            SpecialistDoctorName=Doctor.objects.get(specialization_id=request.session['SpecialistId'],id=request.session['SpecialistDoctorId'])
            
            AppointmentTime=["10:00","10:30","11:00","11:30","12:00","13:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30"]
            appointmentData=Appointment.objects.filter(doctorId=request.session['SpecialistDoctorId'],status="Pending")
            # Remove the time slots that are already booked under a specific doctor
            for i in appointmentData:
                if i.appointmentTime in AppointmentTime:
                    AppointmentTime.remove(i.appointmentTime)
            TimeSelected=appointmentTime
            request.session['AppointmentTime']=appointmentTime
            return render(request,'patient_book_appointment.html',{"SpecializationList":SpecializationList,"SpecializedDoctorList":SpecializedDoctorList,"SpecialistSelected":SpecialistSelected,"SpecialistDoctorName":SpecialistDoctorName,"AppointmentTime":AppointmentTime,"TimeSelected":TimeSelected})
        else:
            return render(request,'patient_book_appointment.html',{"message":"Please select the specialist type and the doctor you want to book an appointment with.","SpecializationList":SpecializationList})
    else:
        return redirect('PatientLogin')

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
