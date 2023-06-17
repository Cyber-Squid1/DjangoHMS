from django.urls import path
from HMS.views import *

urlpatterns = [
    path('',Home,name='Home'),
    path('adminLogin/',AdminLogin,name='AdminLogin'),
    path('doctorLogin/',DoctorLogin,name='DoctorLogin'),
    path('patientLogin/',PatientLogin,name='PatientLogin'),
    path('adminSignup/',AdminSignup,name='AdminSignup'),
    path('doctorSignup/',DoctorSignup,name='DoctorSignup'),
    path('doctorDashboard/',DoctorDashboard,name='DoctorDashboard'),
    path('doctorpatient/',DoctorPatient,name='DoctorPatient'),
    path('doctorViewAppointment/',DoctorViewAppointment,name='DoctorViewAppointment'),
    path('viewAllPatientRecord/',ViewAllPatientRecords,name='ViewAllPatientRecords'),
    path('viewYourPatientRecord/',ViewYourPatientRecords,name='ViewYourPatientRecords'),
    path('viewSinglePatientRecord/<int:patientId>/<int:x>',ViewSinglePatientRecord,name='ViewSinglePatientRecord'),
    path('viewAllAdmittedPatients/',ViewAllAdmittedPatients,name='ViewAllAdmittedPatients'), # TODO: create a list of dictionaries for admitted patients details
    path('viewAdmittedPatient/<int:appointmentId>',ViewAdmittedPatientDetails,name='ViewAdmittedPatientDetails'),
    path('updateDischargePatient/',UpdateDischargePatient,name='UpdateOrDischargePatient'),
    path('appointmentComplete/<int:patientId>/',AppointmentComplete,name='AppointmentComplete'),
    path('patientSignup/',PatientSignup,name='PatientSignup'),
    path('Logout/',Logout,name='Logout'),
    path('patientDashboard/',PatientDashboard,name='PatientDashboard'),
    path('bookAppointment/',PatientBookAppointment,name='PatientBookAppointment'),
    path('bookAppointment/<int:doctorSpecialization>',ShowDoctors,name='ShowDoctors'),
    path('bookAppointment/<int:doctorSpecialization>/<int:doctorId>/',SelectDoctor,name='SelectDoctor'),
    path('bookAppointment/<str:appointmentTime>',SelectTime,name='SelectTime'),
    path('confirmAppointment/',ConfirmAppointment,name='ConfirmAppointment'),
    path('viewAppointment/',PatientViewAppointment,name='PatientViewAppointment'),
    path('contactUs/',ContactUs,name='ContactUs'),
]
