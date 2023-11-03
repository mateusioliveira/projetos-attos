from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    year = models.IntegerField()
    category = models.CharField(max_length=50)
    last_updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.user.username

class InstagramProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    instagram_link = models.URLField()
    nomeRede = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True)

class Fotos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='fotos/')

class quantidadeDoadores(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    quantidade_doadores = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username