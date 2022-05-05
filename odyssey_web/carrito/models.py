from itertools import product
from unicodedata import decimal
import uuid
import decimal
from django.db import models
from user.models import Usuario
from producto.models import Producto
from django.db.models.signals import pre_save
from django.db.models.signals import m2m_changed


# Create your models here.

class Carrito(models.Model):
    carro_id = models.CharField(max_length=100, null = False, blank=False, unique=True)
    user =  models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Producto)
    subtotal = models.DecimalField(default=0.0, max_digits = 8, decimal_places=2)
    total = models.DecimalField(default=0.0, max_digits = 8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    FEE = 0.05 #comision IVA

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

def set_cart_id(sender, instance, *args, **kwars):
    if not instance.carro_id:
        instance.carro_id = str(uuid.uuid4())

def update_totals(sender, instance, action, *args, **kwars):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        instance.update_totals()

pre_save.connect(set_cart_id, sender=Carrito)
m2m_changed.connect(update_totals, sender=Carrito.products.through)

class Detalle_compra(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    id_producto = models.CharField(max_length=50)
    rut_cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    precio_producto = models.IntegerField()
    cantidad = models.IntegerField(null = True)
    
    def __str__(self):
        return self.nombre
