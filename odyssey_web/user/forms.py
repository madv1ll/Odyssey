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
        if commit:
            user.save()
            return user
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