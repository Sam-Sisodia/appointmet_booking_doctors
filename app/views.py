# from django.shortcuts import render
# from django.views import View
# from app.models import Doctor, Appointment
# from app.email import appointment_mail
# from django.contrib import messages
# from datetime import datetime

from django.shortcuts import render, redirect
from django.views import View
from django.utils import timezone
from datetime import datetime
from .models import Doctor, Appointment
from .email import appointment_mail
from django.contrib import messages

class BookAppointment(View):
    def get(self, request):
        doctors = Doctor.objects.all()
        context = {
            "doctors": doctors
        }
        return render(request, "home.html", context)
    
    def post(self, request):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        doctor_id = request.POST.get("doctor")
        message = request.POST.get("message")
        date = request.POST.get("date")
        time = request.POST.get("time")

        validation_result = self.validate_appointment(doctor_id,date, time,)
        if validation_result:
            messages.error(request, f"{validation_result}.")
            return redirect('home')  # Assuming 'home' is the name of the URL pattern for the home page
        
        if date:
            doctor = Doctor.objects.get(id=doctor_id)
            appointment = Appointment.objects.create(doctor=doctor, name=name, email=email, phone=phone,
                                                      message=message, date=date, time=time)
            appointment_mail(appointment, doctor)
            messages.success(request, f"Your appointment is booked at {appointment.date} {appointment.time}")
        
        return redirect('home')  # Redirect to the home page after processing the form
    
    @staticmethod
    def validate_appointment(doctor_id,date, time_str):
        if Appointment.objects.filter(doctor= doctor_id, time=time_str,date=date).exists():
            return "Already Booke please select another one slot of time "

        selected_datetime = datetime.strptime(date + ' ' + time_str, '%Y-%m-%d %H:%M')
        current_datetime = datetime.now()

        if not doctor_id:
            return "Select  Your Doctor"

        if selected_datetime <= current_datetime:
            return "Please select a future time"

        if selected_datetime.date() <= current_datetime.date():
            return "Please select today's date"

        return None  # Return None if no validation errors occur

# Create your views here.



# class BookAppointment(View):
#     def get(self,request):
#         doctors = Doctor.objects.all()
#         current_date = datetime.today().date()
#         current_time = datetime.now().time()
#         print("Current Date:", current_date,"++++++++++++++++++++++++",current_time)


#         context = {
#             "doctors":doctors
#         }
#         return render(request , "home.html" , context)
    
#     def post(self,request):
#         name = request.POST.get("name")
#         phone = request.POST.get("phone")
#         email = request.POST.get("email")
#         doctor = request.POST.get("doctor")
#         print("+++++++++++",doctor)
#         message = request.POST.get("message")
#         date = request.POST.get("date")
#         time = request.POST.get("time")


#         jj =BookAppointment.validate_appointment(date,time) 
#         if jj:
#             print("++++++",jj)
#             messages.error(request, f" {jj}Please select the correct time and date")
         
        
        
        
#         if date:
#             obj = Appointment.objects.create(doctor_id= doctor , name= name , email= email , phone=phone, message= message,date=date,
#                                             time = time)
#             doctor_mail = Doctor.objects.get(id=obj.doctor.id)
#             appointment_mail(obj,doctor_mail)
#             messages.add_message(request,messages.SUCCESS,f"Your Appointment  is booked at{obj.date} {obj.time}  ")
#             #return render(request, 'show.html'
       
#         return render(request, "home.html")
    
#     @staticmethod
#     def validate_appointment(date,time):
#         if datetime.now().strftime('%H:%M') != time:
#             return   "Please select the correct time and date"
          
#         if datetime.now().date() != datetime.strptime(date, '%Y-%m-%d').date():
#             return  "Please select today's date"
          

       

        


