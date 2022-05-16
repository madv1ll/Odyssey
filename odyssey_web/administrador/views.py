from django.shortcuts import render
from carrito.models import Compra, Detalle_compra

def administrador(request):
    return render(request, 'admin.html')


def listar_compra(request):
    compra = Compra.objects.all()
    return render(request, 'registrosCompra/lista_compras.html', {'entity':compra})

def listar_productosCompra(request, id):
    productosCompra = Detalle_compra.objects.filter( id_compra=id)
    return render(request, 'registrosCompra/lista_productosCompra.html', {'entity':productosCompra})