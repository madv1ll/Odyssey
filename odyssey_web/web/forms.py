from django import forms
from .models import ImagenLogo

class LogoForm(forms.ModelForm):
    class Meta:
        model = ImagenLogo
        fields = '__all__'
