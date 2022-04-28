from django.db import models
from web.models import Pais, Region, Comuna

# class Pais(models.Model):
#     id_pais = models.AutoField(primary_key=True)
#     sigla   = models.CharField(max_length=3)
#     nombre  = models.CharField(max_length=60,null=False)

#     def __str__(self):
#         return self.nombre

# class Region(models.Model):
#     id_region = models.AutoField(primary_key=True)
#     nombre    = models.CharField(max_length=60)
#     id_pais   = models.ForeignKey(Pais, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.nombre

# class Comuna(models.Model):
#     id_comuna = models.AutoField(primary_key=True)
#     sigla     = models.CharField(max_length=3)
#     nombre    = models.CharField(max_length=30)
#     id_region   = models.ForeignKey(Region, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.nombre

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    rut          = models.CharField(max_length=12, null=True) 
    nombre       = models.CharField(max_length=50, null=False)
    id_pais      = models.ForeignKey(Pais, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre 

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=30)

    def __str__(self):
        return self.descripcion

#-------------------------------PENDIENTE

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50) # AGREGAR AL MODELO!!!!!!!!!!
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="productos", null=True)
    precio = models.IntegerField()
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    stock = models.IntegerField(null = True)
    
    def __str__(self):
        return self.nombre
