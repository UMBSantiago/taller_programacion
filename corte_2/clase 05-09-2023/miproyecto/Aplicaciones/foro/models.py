# En 'models.py' de la aplicación 'foro'
from django.db import models

class Foro(models.Model):
    autor = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    #fecha = models.DateTimeField(auto_now=True)


