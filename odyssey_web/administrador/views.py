from django.shortcuts import render
from carrito.models import Compra, Detalle_compra


def administrador(request):
    if request.user.is_staff:
        print("es administrador")
        return render(request, 'admin.html')
    else:
        print("no es administrador")    
        return render(request, 'acceso-denegado.html')


def listar_compra(request):
    compra = Compra.objects.all()
    if request.user.is_staff:
        return render(request, 'registrosCompra/lista_compras.html', {'entity':compra})
    else:    
        return render(request, 'acceso-denegado.html')    

def listar_productosCompra(request, id):
    productosCompra = Detalle_compra.objects.filter( id_compra=id)
    if request.user.is_staff:
        return render(request, 'registrosCompra/lista_productosCompra.html', {'entity':productosCompra})
    else:    
        return render(request, 'acceso-denegado.html')    