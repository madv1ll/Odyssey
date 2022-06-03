from ast import Return
import re
from django import forms
from django.db import models
from django.db.models import fields
from django.forms import  ValidationError, widgets

from web.models import Pais
from .models import  Proveedor, Categoria, Producto


class ProveedorForm(forms.ModelForm):
    nombre = forms.CharField(min_length=3, max_length=50)
    rut = forms.IntegerField(min_value=10000000, max_value= 99999999)
    id_pais = forms.ModelChoiceField(queryset=Pais.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}),label='Pais')

    def clean_nombre(self):
        nombreR = self.cleaned_data["nombre"]
        existe = Proveedor.objects.filter(nombre__iexact=nombreR).exists()
        if existe:
            raise ValidationError("Este nombre ya existe")
        return nombreR.upper()

    class Meta:
        model = Proveedor
        fields = '__all__'

class ProveedorEditForm(forms.ModelForm):
    nombre = forms.CharField(min_length=3, max_length=50)
    rut = forms.CharField(min_length=8, max_length=8)
    
    def clean_nombre(self):
        nombreR = self.cleaned_data["nombre"]
        existe = Proveedor.objects.filter(nombre__iexact=nombreR).exists()
        if existe:
            raise ValidationError("Este nombre ya existe")
        return nombreR.upper()
    class Meta:
        model = Proveedor
        fields = '__all__'   

class CategoriaForm(forms.ModelForm):
    descripcion = forms.CharField(min_length=3, max_length=30)
    def clean_descripcion(self):
        descrip_cleaned = self.cleaned_data["descripcion"]
        return descrip_cleaned.upper()

    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    # geeks_field = forms.RegexField(regex = "G.*s") 
    nombre = forms.CharField(min_length=3, max_length=50)
    precio = forms.IntegerField(min_value=1, max_value= 999999999)
    stock = forms.IntegerField(min_value=0, max_value= 999)
    id_categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}),label='Categoría')
    id_proveedor = forms.ModelChoiceField(queryset=Proveedor.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}),label='Proveedor')

    def clean_nombre(self):
        nombreR = self.cleaned_data["nombre"]
        existe = Producto.objects.filter(nombre__iexact=nombreR).exists()
        
        if existe:
            raise ValidationError("Este nombre ya existe")
        return nombreR.upper()

    def caracteresRegulares(self):
        nombre = self.cleaned_data["nombre"]
        print(re.search("milo",nombre))

    def clean_descripcion(self):
        desc_cleaned = self.cleaned_data["descripcion"]
        return desc_cleaned.upper()
    class Meta:
        model = Producto
        fields = '__all__'



class ProductoEditForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
