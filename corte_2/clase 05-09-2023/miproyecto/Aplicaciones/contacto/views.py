from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.conf import settings

from .models import Contacto

# Create your views here.
def contacto(request):
    if request.method == "POST":
        tname = request.POST["name"]
        temail = request.POST["email"]
        tphone = request.POST["phone"]
        tmessage = request.POST["message"]
        obj_contact = Contacto(name=tname,email=temail,phone=tphone,message=tmessage)
        obj_contact.save()
        #return HttpResponse("EL registro fue ingresado")
        email(obj_contact)
        return render(request,"pages/gracias.html",)

    return render(request,"pages/contacto.html",)

def email(email):
    subject = 'Gracias por contactarnos'
    message = ' Este es un correo de verificación '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email.email,]
    send_mail( subject, message, email_from, recipient_list )
    return True
    



#https://www.youtube.com/watch?v=tOEFOnLzBl4