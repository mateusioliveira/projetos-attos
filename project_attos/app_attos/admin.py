from django.contrib import admin

from .models import UserProfile,InstagramProfile,Fotos

admin.site.register(UserProfile)
admin.site.register(InstagramProfile)
admin.site.register(Fotos)