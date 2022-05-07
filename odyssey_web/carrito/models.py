import decimal
from django.db import models
from user.models import Usuario
from producto.models import Producto
class Carrito(models.Model):
    carro_id = models.CharField(max_length=100, null = False, blank=False, unique=True)
    rut_cliente =  models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)
    producto = models.ManyToManyField(Producto)
    subtotal = models.DecimalField(default=0, max_digits = 8, decimal_places=0)
    total = models.DecimalField(default=0, max_digits = 8, decimal_places=0)
    fecha = models.DateTimeField(auto_now_add=True)

    IVA = 0.19 #comision IVA

    def __str__(self):
        return self.carro_id

    def update_totals(self):
        self.update_subtotal()
        self.update_total()

    def update_subtotal(self):
        self.subtotal = sum([ producto.precio  for producto in self.products.all()]) 
        self.save()  

    def update_total(self):
        self.total = self.subtotal + (self.subtotal * decimal.Decimal(Carrito.FEE))
        self.save()

class Detalle_compra(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    id_producto = models.CharField(max_length=50)
    rut_cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    precio_producto = models.IntegerField()
    cantidad = models.IntegerField(null = True)
    
    def __str__(self):
        return self.nombre
