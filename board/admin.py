from django.contrib import admin
from .models import Patient, MedicalImage

# Register your models here.
admin.site.register(Patient)
admin.site.register(MedicalImage)