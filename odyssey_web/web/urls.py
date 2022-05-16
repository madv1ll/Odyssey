from re import template
from django.urls import path
from .views import home, listar_productosVenta, nosotros

urlpatterns = [
    path('', home, name="home"),
    path('nosotros/', nosotros, name="nosotros"),
    path('productos/', listar_productosVenta, name="productosVenta"),
]
