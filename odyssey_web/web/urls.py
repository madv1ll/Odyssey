from re import template
from django.urls import path
from .views import home, listar_productosVenta, nosotros, agregar_presentacion1, modificar_presentacion1, agregar_presentacion2, \
    modificar_presentacion2, agregar_presentacion3, modificar_presentacion3, detalleProducto


urlpatterns = [
    path('', home, name="home"),
    path('nosotros/', nosotros, name="nosotros"),
    #productos
    path('productos/', listar_productosVenta, name="productosVenta"),
    path('productos/', listar_productosVenta, name="productosVenta"),
    path('detalle_producto/<id>/',detalleProducto, name="detalleProducto"),
    #presentaciones en pestaña nosotros
    path('agregar-presentacion1/', agregar_presentacion1, name="agregar_presentacion1"),
    path('modificar-presentacion1/<id>/', modificar_presentacion1, name="modificar_presentacion1"),
    path('agregar-presentacion2/', agregar_presentacion2, name="agregar_presentacion2"),
    path('modificar-presentacion2/<id>/', modificar_presentacion2, name="modificar_presentacion2"),
    path('agregar-presentacion3/', agregar_presentacion3, name="agregar_presentacion3"),
    path('modificar-presentacion3/<id>/', modificar_presentacion3, name="modificar_presentacion3"),
]
