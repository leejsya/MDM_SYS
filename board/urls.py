from django.urls import path, include
from .views import PatientsAPI, PatientAPI, MedicalImagesAPI, MedicalImageAPI, PatientDetailView

urlpatterns = [
    path('patients/', PatientsAPI.as_view()),
    path('patients/<int:pid>/', PatientDetailView.as_view()),
    path('patients/images/', MedicalImagesAPI.as_view())
]