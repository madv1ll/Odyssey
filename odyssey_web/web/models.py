from django.db import models

class Pais(models.Model):
    id_pais = models.AutoField(primary_key=True)
    sigla   = models.CharField(max_length=3)
    nombre  = models.CharField(max_length=60,null=False)

    def __str__(self):
        return self.nombre

class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre    = models.CharField(max_length=60)
    id_pais   = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    sigla     = models.CharField(max_length=3)
    nombre    = models.CharField(max_length=30)
    id_region   = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Presentacion1(models.Model):
    id_presentacion = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=410 )
    ubicacion_img = models.CharField(max_length=20, default="Derecha")
    imagen = models.ImageField(upload_to="logo", null=True)

    def __str__(self):
        return self.nombre

class Presentacion2(models.Model):
    id_presentacion = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=410 )
    ubicacion_img = models.CharField(max_length=20, default="Derecha")
    imagen = models.ImageField(upload_to="logo", null=True)

    def __str__(self):
        return self.nombre 

class Presentacion3(models.Model):
    id_presentacion = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=410)
    ubicacion_img = models.CharField(max_length=20, default="Derecha")
    imagen = models.ImageField(upload_to="logo", null=True)

    def __str__(self):
        return self.nombre        


      
