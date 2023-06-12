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
    path('bookAppointment/',PatientBookAppointment,name='PatientBookAppointment'),
    path('bookAppointment/<str:doctorSpecialization>',ShowDoctors,name='ShowDoctors'),
    path('bookAppointment/<str:doctorSpecialization>/<str:doctorName>',SelectDoctor,name='SelectDoctor'),
    path('confirmAppointment/',ConfirmAppointment,name='ConfirmAppointment'),
    path('viewAppointment/',PatientViewAppointment,name='PatientViewAppointment'),
    path('contactUs/',ContactUs,name='ContactUs'),
]
