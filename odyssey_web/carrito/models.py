import decimal
from django.db import models
from user.models import Usuario, Direccion
from producto.models import Producto
class Tipo_Pago(models.Model):
    id_tipo_pago = models.AutoField(primary_key=True)
    nombre       = models.CharField(max_length=20)
class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    rut_usuario =  models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_pago_pago = models.CharField(max_length=3,null=False)
    id_direccion = models.IntegerField()
    total = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    cant_cuotas  = models.IntegerField(null=True)
    monto_cuotas = models.IntegerField(null=True)

class Detalle_compra(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    id_producto = models.CharField(max_length=50)
    rut_cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    precio_producto = models.IntegerField()
    cantidad = models.IntegerField(null = True)
    
    def __str__(self):
        return self.nombre
