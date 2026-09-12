from rest_framework import serializers
from .models import Patient, MedicalImage

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['pid',
                  'name',
                  'gender',
                  'age',
                  'registered_time'
        ]

class MedicalImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalImage
        fields = ['img_id',
                  'patient',
                  'image',
                  'taken_time',
                  'description',
        ]