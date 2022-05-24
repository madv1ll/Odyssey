from django import forms
from .models import Presentacion1, Presentacion2, Presentacion3

FAVORITE_COLORS_CHOICES = [
    ('Derecha', 'Derecha'),
    ('Izquierda', 'Izquierda'),
]

class Presentacion1Form(forms.ModelForm):
    ubicacion_img = forms.ChoiceField(
    required=True,
    widget=forms.RadioSelect,
    choices=FAVORITE_COLORS_CHOICES,
    label='Ubicacion de imagen en pantalla',
    )

    class Meta:
        model = Presentacion1
        fields = '__all__'

class Presentacion2Form(forms.ModelForm):
    ubicacion_img = forms.ChoiceField(
    required=True,
    widget=forms.RadioSelect,
    choices=FAVORITE_COLORS_CHOICES,
    label='Ubicacion de imagen en pantalla',
    )
    class Meta:
        model = Presentacion2
        fields = '__all__'        

class Presentacion3Form(forms.ModelForm):
    ubicacion_img = forms.ChoiceField(
    required=True,
    widget=forms.RadioSelect,
    choices=FAVORITE_COLORS_CHOICES,
    label='Ubicacion de imagen en pantalla',
    )
    class Meta:
        model = Presentacion3
        fields = '__all__'             
