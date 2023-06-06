from django.shortcuts import render
from .models import Usuario

# Create your views here.

def landing_page(request):
    return render(request, 'index.html')

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})

