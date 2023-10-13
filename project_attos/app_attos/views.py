from .models import InstagramProfile
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404,redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile

index_page_html =  "app_attos/index.html"

def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/perfil/")
    else:
        return render(request, index_page_html)
    

def pagina_da_ong(request, slug):
    usuario = User.objects.get(username=slug)
    user_profile = get_object_or_404(UserProfile, user__username=slug)
    profiles = InstagramProfile.objects.filter(user=usuario)

    if usuario:
        return render(request, "pages/page.html", {"usuario": usuario, "user_profile": user_profile, 'profiles': profiles})



def pagina_de_cadastro(request):
    return render(request, "cadastro/cadastro.html")

def pagina_de_perfil(request):
    if request.user.is_authenticated:
        profiles = instagram_button(request)
        return render(request, "perfil/perfil.html", {'profiles': profiles})
    else:
        return HttpResponseRedirect("/")


@login_required
def instagram_button(request):
    if request.method == 'POST':
        instagram_link = request.POST.get('instagram_link')
        nomeRede = request.POST.get('nomeRede')        
        instagram_profile = InstagramProfile(user=request.user, instagram_link=instagram_link, nomeRede=nomeRede)
        instagram_profile.save()
    profiles = InstagramProfile.objects.filter(user=request.user)
    return profiles


@require_POST
def cadastrar_usuario(request):
    try:
        usuario_aux = User.objects.get(email=request.POST['email'])

        if usuario_aux:
            return render(request, 'cadastro/cadastro.html', {'msg': 'Erro! Já existe um usuário com o mesmo e-mail'})

    except User.DoesNotExist:
        nome_usuario = request.POST['nome-usuario']
        email = request.POST['email']
        senha = request.POST['senha']
        telefone = request.POST['telefone']
        endereco = request.POST['endereco']
        ano_fundacao = request.POST['ano_fundacao']
        categoria = request.POST['categoria']

        novoUsuario = User.objects.create_user(username=nome_usuario, email=email, password=senha)
        novoUsuario.save()
        UserProfile.objects.create(user=novoUsuario, phone=telefone, address=endereco, year=ano_fundacao, category=categoria)

        login(request, novoUsuario)

        return HttpResponseRedirect("/perfil/")

@require_POST
def entrar(request):
    usuario_aux = User.objects.get(email=request.POST['email'])
    usuario = authenticate(username=usuario_aux.username,
                           password=request.POST["senha"])
    if usuario is not None:
        login(request, usuario)
        return HttpResponseRedirect('/perfil/')

    return HttpResponseRedirect("/")

@login_required
def sair(request):
    logout(request)
    return HttpResponseRedirect("/")
