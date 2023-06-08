from django import forms
from .models import Usuario

#en este formulario hay que poner los validadores de las imagens de la clase de 7/6/23

class RegistroUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nombre', 'apellido', 'nombre_usuario', 'correo', 'telefono', 'imagen_perfil')
        widgets = {
            'contraseña': forms.PasswordInput(),
        }
