from django.shortcuts import render
from producto.models import Producto
from django.core.paginator import Page, Paginator
from django.db.models import Q


def home(request):
    return render(request, 'web/home.html')

def listar_productosVenta(request):
    busqueda = request.GET.get("buscar")
    productos = Producto.objects.filter(stock__gt=0)
    if busqueda:
        productos = Producto.objects.filter(
             stock__gt=0 and
            Q(nombre__icontains = busqueda) |
            Q(descripcion__icontains = busqueda)
        ).distinct()
    return render(request, 'web/productos.html', {'entity':productos})