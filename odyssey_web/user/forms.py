from distutils.core import run_setup
from unicodedata import numeric
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from web.models import Comuna, Region
from .models import Usuario, Direccion
#Importaciones para validacion correo
import datetime, random, hashlib
from django.core.mail import send_mail

class UsuarioForm(forms.ModelForm):
    rut = forms.IntegerField(label= 'RUT', widget=forms.NumberInput(
        attrs={
            'class': 'form-control mb-2',
            'placeholder':'Ingrese RUT',
            'max_length': '8'
        }))
    dv = forms.CharField(label= 'DV', max_length=1, widget=forms.TextInput(
        attrs={
            'class': 'form-control mb-2',
            'placeholder':'Ingrese digito verificador',
        }))
    nombre = forms.CharField(label='Nombre',widget=forms.TextInput(
        attrs={
            'class': 'form-control md-3',
            'placeholder':'Ingrese Nombre'
        }))
    apellido = forms.CharField(label='Apellido', widget=forms.TextInput(
        attrs={
            'class': 'form-control md-3',
            'placeholder':'Ingrese Apellido'
        }))
    telefono =  forms.CharField(max_length=9, widget=forms.NumberInput(
        attrs={
            'class': 'form-control md-3',
            'placeholder':'Ingrese Telefono'
        }))
    correo =forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control md-3',
            'placeholder':'Ingrese Correo'
        }))

    password = forms.CharField(label= 'Contraseña', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control md-3',
            'placeholder':'Ingrese Contraseña',
            'id': 'password'
        }))

    class Meta:
        model = Usuario
        fields = ('rut','dv','nombre','apellido','telefono','correo','password')

    def clean_rut(self):
        rut_cleaned = self.cleaned_data.get('rut')
        if len(str(rut_cleaned)) < 7 or len(str(rut_cleaned)) > 8:
            raise forms.ValidationError('Ingrese un RUT válido')
        return rut_cleaned
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('La contraseña debe tener mínimo 8 caracteres.')
        return password
    def clean_dv(self):
        dv_cleaned = self.cleaned_data.get('dv')
        return str(dv_cleaned).upper()
    def clean_correo(self):
        correo_cleaned = self.cleaned_data.get('correo')
        try:
            Usuario._default_manager.get(email=correo_cleaned)
        except Usuario.DoesNotExist:
            return correo_cleaned
        raise forms.ValidationError('email duplicado')

    def save(self,commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        usern = self.cleaned_data['correo']
        user.nombre = self.cleaned_data['nombre'].upper()
        user.apellido = self.cleaned_data['apellido'].upper()
        user.username = usern
        salt = hashlib.sha1(str(random.random()).encode("utf-8")).hexdigest()[:5]          
        key = hashlib.sha1(str(salt+usern).encode("utf-8")).hexdigest()            
        user.activation_key = key
        user.key_expires = datetime.datetime.today() + datetime.timedelta(2)
        
        if commit:
            user.is_active = False
            user.save()
             # Enviar un email de confirmación
            email_subject = 'Confirmacion de Cuenta'
            email_body = "Hola %s, Gracias por registrarte. Para activar tu cuenta da clíck en este link en menos de 48 horas: http://127.0.0.1:8000/user/confirmacion/%s" % (user.nombre.lower(), key)

            send_mail(email_subject, email_body, 'odysseygamming@outlook.com', [usern], fail_silently=False)
        return user


class UsuarioAdminForm(forms.ModelForm):
    rut = forms.IntegerField(label= 'RUT', widget=forms.NumberInput(
        attrs={
            'class': 'form-control mb-2',
            'placeholder':'Ingrese RUT',
            'max_length': '8'
        }))
    dv = forms.CharField(label= 'DV', max_length=1, widget=forms.TextInput(
        attrs={
            'class': 'form-control mb-2',
            'placeholder':'Ingrese digito verificador',
        }))
    nombre = forms.CharField(label='Nombre',widget=forms.TextInput(
        attrs={
            'class': 'form-control md-3',
            'placeholder':'Ingrese Nombre'
        }))
    apellido = forms.CharField(label='Apellido', widget=forms.TextInput(
        attrs={
            'class': 'form-control md-3',
            'placeholder':'Ingrese Apellido'
        }))
    telefono =  forms.CharField(max_length=9, widget=forms.NumberInput(
        attrs={
            'class': 'form-control md-3',
            'placeholder':'Ingrese Telefono'
        }))
    correo =forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control md-3',
            'placeholder':'Ingrese Correo'
        }))

    password = forms.CharField(label= 'Contraseña', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control md-3',
            'placeholder':'Ingrese Contraseña',
            'id': 'password'
        }))
   
    class Meta:
        model = Usuario
        fields = ('rut', 'dv', 'nombre', 'apellido', 'correo', 'telefono', 'is_staff')

    def clean_rut(self):
        rut_cleaned = self.cleaned_data.get('rut')
        if len(str(rut_cleaned)) < 7 or len(str(rut_cleaned)) > 8:
            raise forms.ValidationError('Ingrese un RUT válido')
        return rut_cleaned
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('La contraseña debe tener mínimo 8 caracteres.')
        return password
    def clean_dv(self):
        dv_cleaned = self.cleaned_data.get('dv')
        return str(dv_cleaned).upper()
 
    def save(self,commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        usern = self.cleaned_data['correo']
        user.nombre = self.cleaned_data['nombre'].upper()
        user.apellido = self.cleaned_data['apellido'].upper()
        user.username = usern
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
    calle = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' }))
    numero = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control' }))
    region = forms.ModelChoiceField(queryset=Region.objects.all(), widget=forms.Select(attrs={'class': 'form-control' }))
    id_comuna = forms.ModelChoiceField(queryset=Comuna.objects.all(), widget=forms.Select(attrs={'class': 'form-control' , 'hidden' : 'true'}),label='Comuna')
    principal = forms.ChoiceField(
    required=True,
    widget=forms.RadioSelect,
    choices=FAVORITE_COLORS_CHOICES,
    label='Direccion Principal',
    )

    def clean_calle(self):
        calle_cleaned = self.cleaned_data.get('calle')
        return calle_cleaned.upper()
    class Meta:
        model = Direccion
        fields = ('id_direccion','calle','numero','region','id_comuna','principal')
        
