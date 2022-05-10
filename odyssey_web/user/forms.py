from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import User

from .models import Usuario

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

from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Correo'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'
#-------------------------------
# class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(max_length=140, required=True)
#     last_name = forms.CharField(max_length=140, required=False)
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = (
#             'username',
#             'email',
#             'first_name',
#             'last_name',
#             'password1',
#             'password2',
#         )