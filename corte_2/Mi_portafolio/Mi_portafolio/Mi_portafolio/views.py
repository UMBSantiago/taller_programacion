from django.shortcuts import render

def inicio(request):
    """Retorna gestion pagina de inicio"""
    return render(request,"pages/inicio.html",{})