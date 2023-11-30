from django import forms
from .models import Fotos, Reviews, UserProfile, InstagramProfile

class OngForm(forms.ModelForm):
    class Meta:
        model = Fotos
        fields = ['foto']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['nome', 'email', 'comentario']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email', 'perfil']

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = False
        self.fields['perfil'].required = False

class InstagramProfileForm(forms.ModelForm):
    class Meta:
        model = InstagramProfile
        fields = ['instagram_link', 'nomeRede']

    def __init__(self, *args, **kwargs):
        super(InstagramProfileForm, self).__init__(*args, **kwargs)
        self.fields['instagram_link'].required = False
        self.fields['nomeRede'].required = False

class FotosForm(forms.ModelForm):
    class Meta:
        model = Fotos
        fields = ['foto']

    def __init__(self, *args, **kwargs):
        super(FotosForm, self).__init__(*args, **kwargs)
        self.fields['foto'].required = False

        fields = ['foto']
