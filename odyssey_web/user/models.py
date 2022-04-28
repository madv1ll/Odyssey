from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from web.models import Pais, Region, Comuna

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20, null=True)
    apellido = models.CharField(max_length=20)

    # Python 3
    def __str__(self): 
        return self.usuario.username

@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.perfil.save()

class Direccion(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    calle        = models.CharField(max_length=50, null=False)
    numero       = models.CharField(max_length=20, null=False)
    id_comuna    = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    id_usuario   = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    principal    = models.BooleanField(null=False)