from django.contrib import admin

from django.contrib import admin
from producto.models import Producto, Proveedor, Categoria


# Register your models here.
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Categoria)
