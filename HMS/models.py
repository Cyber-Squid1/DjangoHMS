from django.db import models

# Create your models here.

class Doctor(models.Model):
    doctorName=models.CharField(max_length=200)
    doctorEmail=models.EmailField()
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=200)
    address=models.CharField(max_length=300)
    doctorProfileImg=models.ImageField(upload_to='doctorProfileImg')
    specialization=models.CharField(max_length=200)
    
    def __str__(self):
        return self.doctorName

class Patient(models.Model):
    patientName=models.CharField(max_length=200)
    patientEmail=models.EmailField()
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=200)
    address=models.CharField(max_length=300)
    patientProfileImg=models.ImageField(upload_to='patientProfileImg')
    symptoms=models.CharField(max_length=1000)
    currentlyAssignedDoctorId=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patientMedicalReport=models.ImageField(upload_to='patientMedicalReports/<int:Patient.pk>')
    
    def __str__(self):
        return self.patientName

class Appointment(models.Model):
    doctorId=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patientId=models.ForeignKey(Patient,on_delete=models.CASCADE)
    appointmentDate=models.DateField(auto_now=True)
    description=models.TextField(max_length=2000)
    medicinePrescribed=models.CharField(max_length=1000)
    appointmentCost=models.IntegerField()
    wasAdmitted=models.BooleanField(default=False)
    
    def __str__(self):
        return self.doctorId

class AdmittedPatientDetails(models.Model):
    appointmentDetailsId=models.ForeignKey(Appointment,on_delete=models.CASCADE)
    patientId=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctorIdId=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    admittedOn=models.DateField()
    dischargeDate=models.DateField()
    roomCharges=models.IntegerField()
    MedicineCost=models.IntegerField()
    doctorFees=models.IntegerField()
    otherCharges=models.IntegerField()
    totalCost=models.IntegerField()
    
    def __str__(self):
        return self.appointmentDetailsId
    