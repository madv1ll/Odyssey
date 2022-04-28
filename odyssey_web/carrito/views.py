from django.shortcuts import render
from .carro import Carro
from producto.models import Producto
from django.shortcuts import  redirect

# Create your views here.
def agre_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id = producto_id)
    carro.agregar(producto = producto)
    return redirect("productosVenta")

def sumar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id = producto_id)
    carro.agregar(producto = producto)
    return redirect("carrito")    


def restar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id =producto_id)
    carro.restar_producto(producto= producto)
    return redirect("carrito")


def limpiar_carro(request):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect("carrito")  

