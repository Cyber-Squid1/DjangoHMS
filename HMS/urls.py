from django.urls import path
from HMS.views import *

urlpatterns = [
    path('',Home,name='Home'),
    path('adminLogin/',AdminLogin,name='AdminLogin'),
    path('doctorLogin/',DoctorLogin,name='DoctorLogin'),
    path('patientLogin/',PatientLogin,name='PatientLogin'),
    path('adminSignup/',AdminSignup,name='AdminSignup'),
    path('doctorSignup/',DoctorSignup,name='DoctorSignup'),
    path('patientSignup/',PatientSignup,name='PatientSignup'),
    path('patientLogout/',PatientLogout,name='Logout'),
    path('patientDashboard/',PatientDashboard,name='PatientDashboard'),
    path('contactUs/',ContactUs,name='ContactUs'),
]
