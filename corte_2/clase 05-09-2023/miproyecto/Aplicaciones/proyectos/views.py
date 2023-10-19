from django.shortcuts import render
from .models import Proyecto

def proyectos(request):
    mis_proyectos = Proyecto.objects.all()
    image_paths = ['images/imagen1.jpg', 'images/imagen2.png', 'images/imagen3.jpg']
    return render(request, "proyectos.html", {"proyectos": mis_proyectos, "image_paths": image_paths})
