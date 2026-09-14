from django.db import models

# Create your models here.

# 환자의 정보를 담고있는 Patient 모델
class Patient(models.Model):
    GENDER_LIST = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    ]
    pid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=1,
                              choices=GENDER_LIST,   # GENDER_LIST에서 choice하도록 설정.
                              default='M')  # 초기값은 'M'으로 설정
    age = models.IntegerField()
    registered_time = models.DateTimeField(auto_now_add=True)  # 환자정보를 post할 시 자동으로 현재 시각이 저장되도록 설정.

    def __str__(self):
        return self.name

# 이미지에 대한 메타 정보를 담고있는 MedicalImage 모델
class MedicalImage(models.Model):
    img_id = models.IntegerField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='images')  # Patient 모델을 참조하도록 설정.
    image = models.ImageField(upload_to='images/')
    taken_time = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
