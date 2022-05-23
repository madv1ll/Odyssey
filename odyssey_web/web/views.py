from django.shortcuts import render, redirect, get_object_or_404
from producto.models import Producto
from .forms import LogoForm
from django.core.paginator import Page, Paginator
from django.db.models import Q
from django.contrib import messages
from .models import ImagenLogo


def home(request):
    img_logo = ImagenLogo.objects.all()
    return render(request, 'web/home.html')

def nosotros(request):
    img_logo = ImagenLogo.objects.all()
    return render(request, 'web/nosotros.html',{'img_logo': img_logo}
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



def agregar_logo(request):
    if request.user.is_staff: 
        data = {
            'form' : LogoForm()
        }
        if request.method == 'POST':
            formulario = LogoForm(data=request.POST,  files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Proveedor Creado correctamente")
                return redirect(to="home")
            data["form"] = formulario   
        return render(request, 'logo/agregar_logo.html', data)
    else:
        return render(request,'acceso-denegado.html')        

def modificar_logo(request, id):
    if request.user.is_staff:
        producto = get_object_or_404(ImagenLogo, id_imagen=id)
        data = {
            'form': LogoForm(instance=producto)
        }
        if request.method == 'POST':
            formulario = LogoForm(data=request.POST, instance=producto, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                
                return redirect(to="nosotros")
            else:
                data["form"] = formulario
        return render(request, 'logo/modificar_logo.html', data)
    else:
        return render(request,'acceso-denegado.html') 
