from django.shortcuts import render, redirect, get_object_or_404
from producto.models import Producto
from .forms import Presentacion1Form, Presentacion2Form, Presentacion3, Presentacion3Form
from django.core.paginator import Page, Paginator
from django.db.models import Q
from django.contrib import messages
from .models import Presentacion1, Presentacion2, Presentacion3


def home(request):
    return render(request, 'web/home.html')

def nosotros(request):
    presentacion1 = Presentacion1.objects.all()
    presentacion2 = Presentacion2.objects.all() 
    presentacion3 = Presentacion3.objects.all()
    return render(request, 'web/nosotros.html',{'presentacion1': presentacion1, 'presentacion2':presentacion2, 'presentacion3':presentacion3}
    )
    

def listar_productosVenta(request):
    busqueda = request.GET.get("buscar")
    productos = Producto.objects.filter(stock__gt=0)
    if busqueda:
        productos = Producto.objects.filter(
            Q(stock__gt = 0) &
            Q(nombre__icontains = busqueda) |
            Q(descripcion__icontains = busqueda)
        ).distinct()
    return render(request, 'web/productos.html', {'entity':productos})



def agregar_presentacion1(request):
    presentacion1 = Presentacion1.objects.all()
    if presentacion1:
         return render(request,'acceso-denegado.html')
    else:

        if request.user.is_staff: 
            data = {
                'form' : Presentacion1Form()
            }
            if request.method == 'POST':
                formulario = Presentacion1Form(data=request.POST,  files=request.FILES)
                if formulario.is_valid():
                    formulario.save()
                    return redirect(to="nosotros")
                data["form"] = formulario   
            return render(request, 'presentacion/agregar_presentacion1.html', data)
        else:
            return render(request,'acceso-denegado.html')        

def modificar_presentacion1(request, id):
    if request.user.is_staff:
        producto = get_object_or_404(Presentacion1, id_presentacion=id)
        data = {
            'form': Presentacion1Form(instance=producto)
        }
        if request.method == 'POST':
            formulario = Presentacion1Form(data=request.POST, instance=producto, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                
                return redirect(to="nosotros")
            else:
                data["form"] = formulario
        return render(request, 'presentacion/modificar_presentacion1.html', data)
    else:
        return render(request,'acceso-denegado.html') 



def agregar_presentacion2(request):
    if request.user.is_staff: 
        data = {
            'form' : Presentacion2Form()
        }
        if request.method == 'POST':
            formulario = Presentacion2Form(data=request.POST,  files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                return redirect(to="nosotros")
            data["form"] = formulario   
        return render(request, 'presentacion/agregar_presentacion2.html', data)
    else:
        return render(request,'acceso-denegado.html')

def modificar_presentacion2(request, id):
    if request.user.is_staff:
        producto = get_object_or_404(Presentacion2, id_presentacion=id)
        data = {
            'form': Presentacion2Form(instance=producto)
        }
        if request.method == 'POST':
            formulario = Presentacion2Form(data=request.POST, instance=producto, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                
                return redirect(to="nosotros")
            else:
                data["form"] = formulario
        return render(request, 'presentacion/modificar_presentacion2.html', data)
    else:
        return render(request,'acceso-denegado.html')           


def agregar_presentacion3(request):
    if request.user.is_staff: 
        data = {
            'form' : Presentacion3Form()
        }
        if request.method == 'POST':
            formulario = Presentacion3Form(data=request.POST,  files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                return redirect(to="nosotros")
            data["form"] = formulario   
        return render(request, 'presentacion/agregar_presentacion3.html', data)
    else:
        return render(request,'acceso-denegado.html')

def modificar_presentacion3(request, id):
    if request.user.is_staff:
        producto = get_object_or_404(Presentacion3, id_presentacion=id)
        data = {
            'form': Presentacion3Form(instance=producto)
        }
        if request.method == 'POST':
            formulario = Presentacion3Form(data=request.POST, instance=producto, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                
                return redirect(to="nosotros")
            else:
                data["form"] = formulario
        return render(request, 'presentacion/modificar_presentacion3.html', data)
    else:
        return render(request,'acceso-denegado.html')           
