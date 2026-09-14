from rest_framework import serializers
from .models import Patient, MedicalImage

# 등록된 patients의 리스트를 보여주는 serializer.
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['pid',
                  'name',
                  'gender',
                  'age',
                  'registered_time'
        ]

# image의 메타 정보를 보여주는 serializer.
class MedicalImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalImage
        fields = ['img_id',
                  'patient',
                  'image',
                  'taken_time',
                  'description',
        ]

# 특정 patient의 detail을 보여주는 serializer.
class PatientDetailSerializer(serializers.ModelSerializer):
    images = MedicalImageSerializer(many=True)  # 한 명의 환자는 여러 이미지를 가질 수 있음.

    class Meta:
        model = Patient
        fields = ['pid',
                  'name',
                  'gender',
                  'age',
                  'registered_time',
                  'images'
        ]