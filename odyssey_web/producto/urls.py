from django.urls import path
from .views import agregar_categoria, agregar_proveedor, eliminar_categoria, eliminar_proveedor, \
                    listar_categoria, listar_productos, agregar_producto, eliminar_producto, listar_proveedor,\
                    modificar_categoria, modificar_producto, modificar_proveedor

urlpatterns = [
    #producto
    path('listar-productos/', listar_productos, name="temp_productos"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    # proveedor
    path('proveedores/', listar_proveedor, name="proveedores"),
    path('agregar-proveedor/', agregar_proveedor, name="agregar_proveedor"),
    path('eliminar-proveedor/<id>/', eliminar_proveedor, name="eliminar_proveedor"),
    path('modificar-proveedor/<id>/', modificar_proveedor, name="modificar_proveedor"),
    # Categoria
    path('listar-categoria/', listar_categoria, name="categorias"),
    path('agregar-categoria', agregar_categoria, name="agregar_categoria"),
    path('eliminar-categoria/<id>/', eliminar_categoria, name="eliminar_categoria"),
    path('modificar-categoria/<id>/', modificar_categoria, name="modificar_categoria"),
]
