from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    year = models.IntegerField()
    category = models.CharField(max_length=50)
    
    def __str__(self):
        return self.user.username

class InstagramProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    instagram_link = models.URLField()
    nomeRede = models.CharField(max_length=100)

class Fotos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Defina o usuário atualmente autenticado como padrão
    foto = models.ImageField(upload_to='fotos/')

    