from re import template
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import home, administrador, listar_proveedor, agregar_proveedor, eliminar_proveedor, modificar_proveedor, \
    modificar_proveedor, listar_categoria, agregar_categoria, eliminar_categoria, modificar_categoria, \
    listar_productos, agregar_producto, eliminar_producto, modificar_producto, registro, listar_productosVenta  

urlpatterns = [
    path('', home, name="home"),
    path('administrador/', administrador, name="administrador"),
    #register
    path('registro/', registro, name="registro"),
    path('login/', LoginView.as_view(template_name = 'user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'web/home.html'), name='logout'),
    # proveedores
    path('proveedores/', listar_proveedor, name="proveedores"),
    path('agregar-proveedor/', agregar_proveedor, name="agregar_proveedor"),
    path('eliminar-proveedor/<id>/', eliminar_proveedor, name="eliminar_proveedor"),
    path('modificar-proveedor/<id>/', modificar_proveedor, name="modificar_proveedor"),
    # Categorias
    path('listar-categoria/', listar_categoria, name="categorias"),
    path('agregar-categoria', agregar_categoria, name="agregar_categoria"),
    path('eliminar-categoria/<id>/', eliminar_categoria, name="eliminar_categoria"),
    path('modificar-categoria/<id>/', modificar_categoria, name="modificar_categoria"),

    # producto
    path('listar-productos/', listar_productos, name="listar_productos"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),


    #web
    path('productos/',listar_productosVenta, name="productos"),




]
