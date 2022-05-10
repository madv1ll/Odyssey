from ast import Return
import re
from django import forms
from django.db import models
from django.db.models import fields
from django.forms import  ValidationError, widgets
from .models import  Proveedor, Categoria, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProveedorForm(forms.ModelForm):
    nombre = forms.CharField(min_length=3, max_length=50)
    rut = forms.CharField(min_length=8, max_length=8)

    def clean_nombre(self):
        nombreR = self.cleaned_data["nombre"]
        existe = Proveedor.objects.filter(nombre__iexact=nombreR).exists() 
        if existe:
            raise ValidationError("Este nombre ya existe")
        return nombreR

    def clean_rut(self):
        rutR = self.cleaned_data["rut"]
        existe = Proveedor.objects.filter(rut__iexact=rutR).exists() 
        if existe:
            raise ValidationError("Este Rut ya existe")
        return rutR


    class Meta:
        model = Proveedor
        fields = '__all__'

class ProveedorEditForm(forms.ModelForm):
    nombre = forms.CharField(min_length=3, max_length=50)
    rut = forms.CharField(min_length=8, max_length=8)
    class Meta:
        model = Proveedor
        fields = '__all__'   

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    # geeks_field = forms.RegexField(regex = "G.*s") 
    nombre = forms.CharField(min_length=3, max_length=50)
    precio = forms.IntegerField(min_value=1, max_value= 999999999)
    stock = forms.IntegerField(min_value=0, max_value= 999)

    def clean_nombre(self):
        nombreR = self.cleaned_data["nombre"]
        existe = Producto.objects.filter(nombre__iexact=nombreR).exists()
        
        if existe:
            raise ValidationError("Este nombre ya existe")
        return nombreR  

    def caracteresRegulares(self):
        nombre = self.cleaned_data["nombre"]
        print(re.search("milo",nombre))    

    class Meta:
        model = Producto
        fields = '__all__'



class ProductoEditForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
