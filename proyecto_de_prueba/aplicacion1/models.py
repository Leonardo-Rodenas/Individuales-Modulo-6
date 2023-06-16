from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nombre_usuario = models.CharField(max_length=100, unique=True, default='usuario')
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    imagen_perfil = models.ImageField(upload_to='static/img/perfil/', blank=True, null=True)

    def __str__(self):
        return self.nombre_usuario  
