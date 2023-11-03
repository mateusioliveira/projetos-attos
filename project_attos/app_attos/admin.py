from django.contrib import admin
from .models import UserProfile,InstagramProfile,Fotos,quantidadeDoadores

admin.site.register(UserProfile)
admin.site.register(InstagramProfile)
admin.site.register(Fotos)
admin.site.register(quantidadeDoadores)  

