
from django.shortcuts import get_object_or_404, redirect, render
from carrito.models import Compra, Detalle_compra
from .forms import CompraEditForm
from django.contrib import messages


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


def modificar_compra(request, id):
    if request.user.is_staff:
        producto = get_object_or_404(Compra, id_compra=id)
        data = {
            'form': CompraEditForm(instance=producto)
        }
        if request.method == 'POST':
            formulario = CompraEditForm(data=request.POST, instance=producto, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "modificado correctamente")
                return redirect(to="lista_compra")
            else:
                data["form"] = formulario
        return render(request, 'registrosCompra/modificar_compra.html', data)
    else:
        return render(request,'acceso-denegado.html')    

