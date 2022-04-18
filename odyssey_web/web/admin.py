from django.contrib import admin
from .models import Producto, Proveedor, Categoria

# Register your models here.
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Categoria)