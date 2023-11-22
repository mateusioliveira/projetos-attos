from django import forms
from .models import Fotos, Reviews

class OngForm(forms.ModelForm):
    class Meta:
        model = Fotos
        fields = ['foto']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['nome', 'email', 'comentario']
