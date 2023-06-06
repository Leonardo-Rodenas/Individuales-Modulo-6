from django.urls import path
from aplicacion1.views import lista_usuarios

urlpatterns = [
    path('usuarios/', lista_usuarios, name='lista_usuarios'),
]
