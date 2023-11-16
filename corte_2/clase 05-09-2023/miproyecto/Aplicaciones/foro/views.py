# En 'views.py' de la aplicación 'foro'
from django.shortcuts import render, redirect,HttpResponse
from .models import Foro

def foro(request):
    if request.method == "POST":
        autor = request.POST["autor"]
        contenido = request.POST["contenido"]

        mensaje = Foro(autor=autor, contenido=contenido)
        mensaje.save()
        # Puedes redirigir a una página de confirmación o a la lista de mensajes
        return render(request, "pagesf/gracias.html",)

    return render(request,"pagesf/foro.html",)

def comentarios(request):
    mis_coment = Foro.objects.all()
    return render(request,"pagesf/comentarios.html",{"comentarios": mis_coment})
