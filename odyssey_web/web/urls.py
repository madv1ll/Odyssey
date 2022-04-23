from re import template
from django.urls import path
from .views import home, listar_productosVenta

urlpatterns = [
    path('', home, name="home"),
    path('productos/', listar_productosVenta, name="productosVenta"),
]
