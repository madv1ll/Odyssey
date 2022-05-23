from re import template
from django.urls import path
from .views import home, listar_productosVenta, nosotros, agregar_logo, modificar_logo

urlpatterns = [
    path('', home, name="home"),
    path('nosotros/', nosotros, name="nosotros"),
    path('productos/', listar_productosVenta, name="productosVenta"),
    path('agregar-logo/', agregar_logo, name="agregar_logo"),
     path('modificar-logo/<id>/', modificar_logo, name="modificar_logo"),
]
