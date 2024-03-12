from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ["id","name","email","on_leave"]



@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ["id","doctor","name","email","phone","message","date","time","availble"]