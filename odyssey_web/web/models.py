from tkinter import Widget
from unittest.util import _MAX_LENGTH
from django import forms
from django.db import models

class Pais(models.Model):
    id_pais = models.AutoField(primary_key=True)
    sigla   = models.CharField(max_length=3)
    nombre  = models.CharField(max_length=60,null=False)

    def __str__(self):
        return self.nombre

class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre    = models.CharField(max_length=60)
    id_pais   = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    sigla     = models.CharField(max_length=3)
    nombre    = models.CharField(max_length=30)
    id_region   = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class ImagenLogo(models.Model):
    id_imagen = models.AutoField(primary_key=True)
    descripcion = models.TextField(forms.Textarea(attrs={"rows":5, "cols":20}), max_length=310 )
    imagen = models.ImageField(upload_to="logo", null=True)

    def __str__(self):
        return self.nombre
