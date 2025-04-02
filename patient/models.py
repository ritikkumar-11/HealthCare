from django.db import models
from doctor.models import Doctor


class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    doctor = models.ManyToManyField(Doctor, related_name='patients')
    
    def __str__(self):
        return self.name
                
