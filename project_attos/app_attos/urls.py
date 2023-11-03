from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cadastrar/", views.pagina_de_cadastro, name='cadastrar'), 
    path("cadastrar_usuario/", views.cadastrar_usuario, name='cadastrar_usuario'),
    path("entrar/", views.entrar, name='entrar'),
    path("sair/", views.sair, name='sair'),
    path("perfil/", views.pagina_de_perfil, name='pagina_de_perfil'),
    path("ong/<str:slug>/", views.pagina_da_ong, name='pagina_da_ong'),
    path('add_foto/', views.add_foto, name='add_foto'),
    path('remover-fotos/', views.remover_fotos, name='remover_fotos'),
    path('adicionar_quantidade_doadores/', views.adicionar_quantidade_doadores, name='adicionar_quantidade_doadores'),
]
