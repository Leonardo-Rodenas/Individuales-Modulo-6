from django.urls import path
from aplicacion1.views import lista_usuarios, registro_usuario

urlpatterns = [
    path('usuarios/', lista_usuarios, name='lista_usuarios'),
    path('formulario/', registro_usuario, name='formulario'),
]
