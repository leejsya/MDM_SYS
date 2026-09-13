from django.db import models

# Create your models here.

class Patient(models.Model):
    GENDER_LIST = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    ]
    pid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=1,
                              choices=GENDER_LIST,
                              default='M')
    age = models.IntegerField()
    registered_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class MedicalImage(models.Model):
    img_id = models.IntegerField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')
    taken_time = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
