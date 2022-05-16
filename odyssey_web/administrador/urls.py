from django.urls import include, path
from .views import administrador, listar_compra, listar_productosCompra

urlpatterns = [
    path('', administrador, name="administrador"),
    path('lista_compra/', listar_compra, name="lista_compra"),
    path('listar_productosCompra/<id>/', listar_productosCompra, name="listar_productosCompra"),
]
