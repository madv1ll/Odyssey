from re import template
from django.urls import path
from .views import home, listar_productosVenta, carrito

urlpatterns = [
    path('', home, name="home"),
    path('productos/', listar_productosVenta, name="productosVenta"),
    #carrito
    path('carrito/', carrito , name= "carrito"),

]
