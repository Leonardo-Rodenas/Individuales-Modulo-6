from django.urls import path
from aplicacion1.views import lista_usuarios, info_usuario
from . import views

urlpatterns = [
    path('usuarios/', lista_usuarios, name='lista_usuarios'),
    path('formulario/', views.formulario_page, name='formulario'),
    path('info/', info_usuario, name='info'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),  
]
