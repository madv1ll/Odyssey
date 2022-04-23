from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from .models import  Proveedor, Categoria, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = '__all__'

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'