from django.contrib import admin
from HMS.models import *
# Register your models here.

class SpecializationRegister(admin.ModelAdmin):
    list_display = ['specialization']
admin.site.register(Specialization,SpecializationRegister)

class DoctorRegister(admin.ModelAdmin):
    list_display = ['doctorName']
admin.site.register(Doctor,DoctorRegister)

admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(AdmittedPatientDetails)
admin.site.register(Feedback)