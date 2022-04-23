from django.shortcuts import render
from producto.models import Producto
from django.core.paginator import Page, Paginator

def home(request):
    return render(request, 'web/home.html')


def listar_productosVenta(request):
    productos = Producto.objects.all()
    data = {
        'entity': productos,
    }
    return render(request, 'web/productos.html', data)