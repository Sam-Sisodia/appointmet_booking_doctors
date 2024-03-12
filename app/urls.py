from django.contrib import admin
from django.urls import path,include
from  . import views

urlpatterns = [
    
    path("", views.BookAppointment.as_view() ,name="home"),
    path("my-data", views.MyAppointments.as_view() ,name="my-data"),
]

