from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
from web.models import Comuna
from django.contrib.auth.models import  AbstractUser, UserManager

class UsuarioManager(UserManager):
    def create_user(self,rut,nombre,apellido, correo, password = None):
        usuario = self.model(
            rut          = rut,
            nombre       = nombre,
            apellido     = apellido,
            correo       = correo,
            username     = correo
        )
        usuario.set_password(password)
        usuario.username(correo)
        usuario.save()
        return usuario

    def create_superuser(self,rut,nombre,apellido, correo, password):
        usuario = self.create_user(
            rut          = rut,
            nombre       = nombre,
            apellido     = apellido,
            correo       = correo,
            username     = correo
        )
        usuario.usuario_administrador = True
        usuario.username(correo)
        usuario.save()
        return usuario


class Usuario(AbstractUser):
    rut                = models.IntegerField(primary_key=True)
    dv                 = models.CharField(max_length=1, null=False)
    nombre             = models.CharField('Nombre',max_length=70, null=False, blank=False)
    apellido           = models.CharField('Apellido',max_length=70, null=False, blank=False)
    correo             = models.EmailField('Correo',max_length=60, null=False, blank=False, unique=True)
    telefono           = models.IntegerField(null=False)
    creacion_fec       = models.DateTimeField('Fecha de ingreso', auto_now_add=True)
    actualizacion_fec  = models.DateTimeField('Fecha actualizacion', auto_now=True)
    USERNAME_FIELD = 'correo'
    class meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return str(self.rut)
    
    def has_perm(self,perm,obj = None):
        return True

    def has_module_perms(self, app_label):
        return True

class Direccion(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    calle        = models.CharField(max_length=50, null=False)
    numero       = models.CharField(max_length=20, null=False)
    id_comuna    = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    id_usuario   = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    principal    = models.CharField(max_length=2,default="SI")

    def direccion_registro(self):
        return "{}{}, {}". format(self.calle, self.numero, self.id_comuna)
    
    
    def __str__(self):
        return self.direccion_registro()
