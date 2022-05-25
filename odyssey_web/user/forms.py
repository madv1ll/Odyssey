from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from web.models import Comuna, Region
from .models import Usuario, Direccion

class UsuarioForm(forms.ModelForm):
    password = forms.CharField(label= 'Contraseña', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder':'Ingrese Contraseña',
            'id': 'password'
        }
    ))
    class Meta:
        model = Usuario
        fields = ('rut', 'nombre', 'apellido', 'correo')

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        return password
 
    def save(self,commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        correo = self.cleaned_data['correo']
        user.username = correo
        if commit:
            user.save()
            return user


class UsuarioAdminForm(forms.ModelForm):
    password = forms.CharField(label= 'Contraseña', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder':'Ingrese Contraseña',
            'id': 'password'
        }
    ))
    class Meta:
        model = Usuario
        fields = ('rut', 'nombre', 'apellido', 'correo', 'is_staff')

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        return password
 
    def save(self,commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        correo = self.cleaned_data['correo']
        user.username = correo
        if commit:
            user.save()
            return user            

from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Correo'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

FAVORITE_COLORS_CHOICES = [
    ('SI', 'Si'),
    ('NO', 'No'),
]

class DireccionForm(forms.ModelForm):
    region = forms.ModelChoiceField(queryset=Region.objects.all(), widget=forms.Select(attrs={'class': 'form-control' }))
    id_comuna = forms.ModelChoiceField(queryset=Comuna.objects.all(), widget=forms.Select(attrs={'class': 'form-control' }))
    principal = forms.ChoiceField(
    required=True,
    widget=forms.RadioSelect,
    choices=FAVORITE_COLORS_CHOICES,
    label='Direccion Principal',
    )
    class Meta:
        model = Direccion
        fields = ('id_direccion','calle', 'numero','principal')
        
