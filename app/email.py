from email import message
from django.core.mail import send_mail
import random
from . models import *

from django.conf  import settings


def appointment_mail(obj,doctor):
    try:

        subject = f'New Appointment Booked  '
        message = f'You have a new appointment booked . By Name: {obj.name}  , Email :{obj.email} , Date : {obj.date} at  Time :{obj.time}' 
        email_from = settings.EMAIL_HOST
        send_mail(subject, message, email_from, [doctor.email])
    except Exception as e:
        print(e)


