from django.db import models

# Create your models here.

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
    symptoms=models.CharField(max_length=1000,default="")
    currentlyAssignedDoctorId=models.CharField(max_length=8,default="")
    patientMedicalReport=models.ImageField(upload_to='patientMedicalReports/<int:Patient.pk>',default="")
    
    def __str__(self):
        return self.patientName

class Appointment(models.Model):
    patientId=models.CharField(max_length=10)
    doctorId=models.CharField(max_length=10)
    appointmentDate=models.DateField(auto_now=True)
    description=models.TextField(max_length=2000)
    medicinePrescribed=models.CharField(max_length=1000)
    appointmentCost=models.IntegerField()
    wasAdmitted=models.BooleanField(default=False)
    
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
    