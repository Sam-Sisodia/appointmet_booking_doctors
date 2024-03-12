from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True,blank=False)
    on_leave = models.BooleanField(default=False) 
    
    def __str__(self) -> str:
        return self.name




class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,null=True,blank=False)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    date = models.DateField()
    time=  models.TimeField()
    availble = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

    
    
