from ast import Return
import re
from django import forms
from django.db import models
from django.db.models import fields
from django.forms import  ValidationError, widgets
from carrito.models import Compra
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

FAVORITE_COLORS_CHOICES = [
    ('Pedido en preparacion', 'Pedido en preparacion'),
    ('Pedido en camino', 'Pedido en camino'),
    ('Pedido entregado', 'Pedido entregado'),

]


class CompraEditForm(forms.ModelForm):
    estado = forms.ChoiceField(
    required=True,
    widget=forms.RadioSelect,
    choices=FAVORITE_COLORS_CHOICES,
    label='Seleccione un estado ',
    )
    class Meta:
        model = Compra
        fields = ('estado',)


