import decimal
from django.db import models
from user.models import Usuario
from producto.models import Producto
import uuid
from django.db.models.signals import pre_save
from django.db.models.signals import m2m_changed
class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    rut_usuario =  models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ManyToManyField(Producto)
    subtotal = models.DecimalField(default=0, max_digits = 8, decimal_places=0)
    total = models.DecimalField(default=0, max_digits = 8, decimal_places=0)
    fecha = models.DateTimeField(auto_now_add=True)

class Detalle_compra(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    id_producto = models.CharField(max_length=50)
    rut_cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    precio_producto = models.IntegerField()
    cantidad = models.IntegerField(null = True)
    
    def __str__(self):
        return self.nombre
