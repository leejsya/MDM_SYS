from rest_framework import generics
from .models import Patient, MedicalImage
from .serializers import PatientSerializer, MedicalImageSerializer, PatientDetailSerializer
from rest_framework import mixins
# Create your views here.
class PatientsAPI(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    lookup_field = 'pid'


class MedicalImagesAPI(generics.ListCreateAPIView):
    serializer_class = MedicalImageSerializer

    def get_queryset(self):
        pid = self.kwargs['pid']
        return MedicalImage.objects.filter(patient_id=pid)

class MedicalImageAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalImage
    serializer_class = MedicalImageSerializer
    lookup_field = 'img_id'

class PatientDetailView(generics.RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientDetailSerializer
    lookup_field = 'pid'
