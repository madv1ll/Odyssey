from django.shortcuts import render
from producto.models import Producto
from django.core.paginator import Page, Paginator
from django.db.models import Q

def home(request):
    return render(request, 'web/home.html')

def listar_productosVenta(request):
    busqueda = request.GET.get("buscar")
    productos = Producto.objects.all()
    if busqueda:
        productos = Producto.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(descripcion__icontains = busqueda)  
        ).distinct()
    return render(request, 'web/productos.html', {'entity':productos})


def carrito(request):
    return render(request, 'carro/carrito.html')     


