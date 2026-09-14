from rest_framework import generics
from .models import Patient, MedicalImage
from .serializers import PatientSerializer, MedicalImageSerializer, PatientDetailSerializer
# Create your views here.

# 등록된 patient 리스트를 보여주고 post할 수 있는 view.
class PatientsAPI(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

# 특정 patient의 detail을 보여주고 수정 및 삭제할 수 있는 view.
class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientDetailSerializer
    lookup_field = 'pid'

# 특정 patient의 이미지 리스트를 보여주고 post할 수 있는 view
class MedicalImagesAPI(generics.ListCreateAPIView):
    serializer_class = MedicalImageSerializer

    def get_queryset(self):
        pid = self.kwargs['pid']  # pid 객체에 요청된 특정 Patient 모델의 pid attribute를 저장.
        return MedicalImage.objects.filter(patient_id=pid)  # 특정 patient의 image만 가져오기.

# 특정 image의 detail을 보여주고 수정 및 삭제할 수 있는 view.
class MedicalImageAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalImage
    serializer_class = MedicalImageSerializer
    lookup_field = 'img_id'

