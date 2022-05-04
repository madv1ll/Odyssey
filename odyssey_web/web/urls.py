from re import template
from django.urls import path
from .views import home, listar_productosVenta, CarritoView,ConfirmacionCompra, DetalleCompra

urlpatterns = [
    path('', home, name="home"),
    path('productos/', listar_productosVenta, name="productosVenta"),
    #carrito
    path('carrito/', CarritoView.as_view(), name='carrito'),
    # path('carrito/', carrito , name= "carrito"),
    path('confirmacion/', DetalleCompra.as_view() , name= "confirmacion"),

]
