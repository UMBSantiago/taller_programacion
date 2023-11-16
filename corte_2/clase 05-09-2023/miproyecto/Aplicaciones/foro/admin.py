# En 'admin.py' de la aplicación 'foro'
from django.contrib import admin
from .models import Foro

admin.site.register(Foro)
