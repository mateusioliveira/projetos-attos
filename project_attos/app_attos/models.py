from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, default='default_email@default.com')
    last_updated = models.DateTimeField(auto_now=True)
    meta_anual = models.FloatField(default=0.00)
    valor_arrecadado = models.FloatField(default=0.00)

    def __str__(self):
        return self.user.username

class InstagramProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    instagram_link = models.URLField()
    nomeRede = models.CharField(max_length=100)

class Fotos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='fotos/')

class quantidadeDoadores(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    quantidade_doadores = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username

class Reviews(models.Model):
    perfil = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    comentario = models.TextField()