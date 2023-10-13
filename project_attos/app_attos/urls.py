from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cadastrar/", views.pagina_de_cadastro, name='cadastrar'), 
    path("cadastrar_usuario/", views.cadastrar_usuario, name='cadastrar_usuario'),
    path("entrar/", views.entrar, name='entrar'),
    path("sair/", views.sair, name='sair'),
    path("perfil/", views.pagina_de_perfil, name='pagina_de_perfil'),
    path("ong/<str:slug>/", views.pagina_da_ong, name='pagina_da_ong')
]
