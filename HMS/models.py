from django.db import models
from django.utils import timezone
# Create your models here.

class Admin(models.Model):
    adminEmail=models.EmailField()
    adminName=models.CharField(max_length=200)
    password=models.CharField(max_length=400)
    
    def __str__(self):
        return self.adminName

class Specialization(models.Model):
    specialization=models.CharField(max_length=200,unique=True,null=False)
    
    def __str__(self):
        return self.specialization

class Doctor(models.Model):
    doctorName=models.CharField(max_length=200)
    doctorEmail=models.EmailField()
    phone=models.BigIntegerField()
    password=models.CharField(max_length=200)
    address=models.CharField(max_length=300)
    doctorProfileImg=models.ImageField(upload_to='doctorProfileImg')
    specialization=models.ForeignKey(Specialization,on_delete=models.CASCADE)
    availableOn=models.CharField(max_length=10,default="")

    def __str__(self):
        return self.doctorName

class Patient(models.Model):
    patientName=models.CharField(max_length=200)
    patientEmail=models.EmailField()
    phone=models.BigIntegerField()
    password=models.CharField(max_length=200)
    address=models.CharField(max_length=300)
    patientProfileImg=models.ImageField(upload_to='patientProfileImg',default="")
    currentlyAssignedDoctorId=models.CharField(max_length=8,default="")
    
    def __str__(self):
        return self.patientName

APPOINTMENT_STATUS=(
    ("PENDING","PENDING"),
    ("COMPLETED","COMPLETED")
)

APPOINTMENT_TIME_CHOICES=(
    ("10:00","10:00"),
    ("10:30","10:30"),
    ("11:00","11:00"),
    ("11:30","11:30"),
    ("12:00","12:00"),
    ("13:30","13:30"),
    ("15:00","15:00"),
    ("15:30","15:30"),
    ("16:00","16:00"),
    ("16:30","16:30"),
    ("17:00","17:00"),
    ("17:30","17:30"),
    ("18:00","18:00"),
    ("18:30","18:30"),
)

class Appointment(models.Model):
    patientId=models.CharField(max_length=10)
    doctorId=models.CharField(max_length=10)
    appointmentDate=models.DateField(auto_now=True)
    appointmentTime=models.CharField(max_length=12,default="",choices=APPOINTMENT_TIME_CHOICES)
    symptoms=models.CharField(max_length=1000,default="")
    medicinePrescribed=models.TextField(max_length=2000)
    appointmentCost=models.IntegerField()
    wasAdmitted=models.BooleanField(default=False)
    description=models.TextField(max_length=2000)
    status=models.CharField(max_length=10,choices=APPOINTMENT_STATUS,default="PENDING")
    
    def __str__(self):
        return self.doctorId

class AdmittedPatientDetails(models.Model):
    appointmentDetailsId=models.CharField(max_length=10)
    patientId=models.CharField(max_length=10)
    doctorId=models.CharField(max_length=10)
    admittedOn=models.DateField()
    dischargeDate=models.DateField()
    roomCharges=models.IntegerField()
    MedicineCost=models.IntegerField()
    doctorFees=models.IntegerField()
    otherCharges=models.IntegerField()
    totalCost=models.IntegerField()
    
    def __str__(self):
        return self.appointmentDetailsId
    

class Feedback(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    phonenumber=models.BigIntegerField()
    message=models.CharField(max_length=1000)
    
    def __str__(self):
        return self.email
    