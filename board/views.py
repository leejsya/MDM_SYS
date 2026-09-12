from rest_framework import generics
from .models import Patient, MedicalImage
from .serializers import PatientSerializer, MedicalImageSerializer
# Create your views here.
class PatientsAPI(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    lookup_field = 'pid'


class MedicalImagesAPI(generics.ListCreateAPIView):
    queryset = MedicalImage.objects.all()
    serializer_class = MedicalImageSerializer

class MedicalImageAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalImage
    serializer_class = MedicalImageSerializer
    lookup_field = 'img_id'
