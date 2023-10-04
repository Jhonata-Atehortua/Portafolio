from django.core.mail import send_mail
from django.shortcuts import render
from .form import Contactanos

def Inicio(request):
    if request.method == "POST":
        formulario = Contactanos(request.POST)
        if formulario.is_valid():
            Asunto = "Persona Interesada"
            Mensaje = "Un usuario se encuentra interesado para hablar contigo"
            Origen = "jhonatanatehortua230@gmail.com"
            Destino = ["jatehortua561@gmail.com"]
            send_mail(Asunto,Mensaje,Origen,Destino)
    
    formulario = Contactanos()
    return render(request,'Portafolio/Inicio.html',{'Formulario':formulario})
