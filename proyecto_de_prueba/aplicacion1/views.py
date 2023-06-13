from django.shortcuts import render, redirect
from .models import Usuario
from aplicacion1.forms import RegistroUsuarioForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def landing_page(request):
    return render(request, 'index.html')

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})

@login_required
def info_usuario (request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('landing_page')  
    else:
        form = RegistroUsuarioForm()

    return render(request, 'info_usuario.html', {'form': form})   

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('formulario')
        else:
            error_message = 'Su usuario o contraseña son incorrectos'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def formulario_page(request):
    username = request.user.username
    return render(request, 'formulario.html', {'username': username})
