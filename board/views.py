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


class MedicalImagesAPI(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = MedicalImage.objects.all()
    serializer_class = MedicalImageSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class MedicalImageAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalImage
    serializer_class = MedicalImageSerializer
    lookup_field = 'img_id'

class PatientDetailView(generics.RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientDetailSerializer
    lookup_field = 'pid'
