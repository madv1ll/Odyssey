from statistics import mode
from django.db import models


class PrecioEnvio(models.Model):
    id_envio = models.AutoField(primary_key=True)
    precio = models.IntegerField()

    def __str__(self):
        return self.precio


class descuentos(models.Model):
    id_descuento = models.AutoField(primary_key=True)
    pregunta = models.CharField(max_length=50)
    respuesta = models.CharField(max_length=50)
    precio = models.IntegerField()

    def __str__(self):
        return self.precio        