# En 'urls.py' de la aplicación 'foro'
from django.urls import path
from . import views

urlpatterns = [
    path('foro/', views.foro, name='foro'),
    path('comentarios/', views.comentarios, name='comentarios'),
    # Agrega más patrones de URL según sea necesario
]
