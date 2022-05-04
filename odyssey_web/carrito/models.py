from itertools import product
from django.db import models
from user.models import Usuario
from producto.models import Producto

# Create your models here.

# class Carrito(models.Model):
#     user =  models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)
#     products = models.ManyToMany(Producto)
#     subTotal = models.DecimalField(default=0.0, max_digits = 8, decimal_places=2)
#     total = models.DecimalField(default=0.0, max_digits = 8, decimal_places=2)


class Detalle_compra(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    id_producto = models.CharField(max_length=50)
    rut_cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    precio_producto = models.IntegerField()
    cantidad = models.IntegerField(null = True)
    
    def __str__(self):
        return self.nombre
