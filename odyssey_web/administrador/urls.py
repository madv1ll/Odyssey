from django.urls import include, path
from .views import administrador, listar_compra, listar_productosCompra, modificar_compra, listar_precioEnvio, modificar_precioEnvio

urlpatterns = [
    path('', administrador, name="administrador"),
    path('lista_compra/', listar_compra, name="lista_compra"),
    path('listar_productosCompra/<id>/', listar_productosCompra, name="listar_productosCompra"),
    path('modificar-compra/<id>/', modificar_compra, name="modificar_compra"),
    #Precio de envio
    path('lista_precioEnvio/', listar_precioEnvio, name="listar_precioEnvio"),
    path('modificar_precioEnvio/<id>/', modificar_precioEnvio, name="modificar_precioEnvio"),
]
