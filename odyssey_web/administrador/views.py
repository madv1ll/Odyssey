
from django.shortcuts import get_object_or_404, redirect, render
from carrito.models import Compra, Detalle_compra
from .forms import CompraEditForm, PrecioEnvioEditForm
from django.contrib import messages
from .models import PrecioEnvio

def administrador(request):
    if request.user.is_staff:
        print("es administrador")
        return render(request, 'admin.html')
    else:
        print("no es administrador")    
        return render(request, 'acceso-denegado.html')


def listar_compra(request):
    compra = Compra.objects.all().order_by('fecha').reverse()
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


#--------------------------- precio envio -------------------------------------

def listar_precioEnvio(request):
    precioEnvio = PrecioEnvio.objects.all()
    if request.user.is_staff:
        return render(request, 'precioEnvio/lista_precio.html', {'entity':precioEnvio})
    else:
        return render(request,'acceso-denegado.html') 


def modificar_precioEnvio(request, id):
    if request.user.is_staff:
        precioEnvio = get_object_or_404(PrecioEnvio, id_envio=id)
        data = {
            'form': PrecioEnvioEditForm(instance=precioEnvio)
        }
        if request.method == 'POST':
            formulario = PrecioEnvioEditForm(data=request.POST, instance=precioEnvio, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "modificado correctamente")
                return redirect(to="listar_precioEnvio")
            else:
                data["form"] = formulario
        return render(request, 'precioEnvio/modificar_precioEnvio.html', data)
    else:
        return render(request,'acceso-denegado.html')    

