from django.shortcuts import render, redirect
from .models import Usuario
from aplicacion1.forms import RegistroUsuarioForm
# Create your views here.

def landing_page(request):
    return render(request, 'index.html')

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('landing_page')  
    else:
        form = RegistroUsuarioForm()

    return render(request, 'formulario.html', {'form': form})
