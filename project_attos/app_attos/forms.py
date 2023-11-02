from django import forms
from .models import Fotos

class OngForm(forms.ModelForm):
    class Meta:
        model = Fotos
        fields = ['foto']
