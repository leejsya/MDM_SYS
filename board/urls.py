from django.urls import path, include
from .views import PatientsAPI, MedicalImagesAPI, MedicalImageAPI, PatientDetailView

urlpatterns = [
    path('patients/', PatientsAPI.as_view()),
    path('patients/<int:pid>/', PatientDetailView.as_view()),
    path('patients/<int:pid>/images/', MedicalImagesAPI.as_view()),
    path('patients/<int:pid>/images/<int:img_id>', MedicalImageAPI.as_view())
]