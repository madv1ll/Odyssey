from django.db import models

# Create your models here.
class Proveedor(models.Model):
    id_proveedor =models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50)
    def __str__(self):
        return self.nombres  

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    Categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.Categoria

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    Proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="productos", null=True)
    stock = models.IntegerField(null = True)
    

    def __str__(self):
        return self.nombre
