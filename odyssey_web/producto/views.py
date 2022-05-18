
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from .forms import CategoriaForm, ProductoForm, ProveedorForm, ProveedorEditForm, ProductoEditForm
from .models import Proveedor, Categoria, Producto
from django.contrib import messages
from django.db.models import Q


#--------------------------productos-----------------------------------------------------

def listar_productos(request):
    busqueda = request.GET.get("buscar")
    productos = Producto.objects.all()
    if busqueda:
        productos = Producto.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(descripcion__icontains = busqueda)  
        ).distinct()
    if request.user.is_staff:
        return render(request, 'producto/listaProducto.html', {'entity':productos})
    else:
        return render(request,'acceso-denegado.html')    
    
def agregar_producto(request):
    if request.user.is_staff:
        data = {
            'form': ProductoForm()
        }
        if request.method == 'POST':
            formulario =ProductoForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Producto Registrado")
            else:
                data["form"] = formulario    
        return render(request, 'producto/agregar_producto.html', data)
    else:
        return render(request,'acceso-denegado.html') 


def eliminar_producto(request, id): 
    if request.user.is_staff:
        producto = get_object_or_404(Producto, id_producto=id)
        producto.delete()
        messages.success(request, "Eliminado correctamente")
        return redirect(to="listar_productos")
    else:
        return render(request,'acceso-denegado.html')       

def modificar_producto(request, id):
    if request.user.is_staff:
        producto = get_object_or_404(Producto, id_producto=id)
        data = {
            'form': ProductoEditForm(instance=producto)
        }
        if request.method == 'POST':
            formulario = ProductoEditForm(data=request.POST, instance=producto, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "modificado correctamente")
                return redirect(to="listar_productos")
            else:
                data["form"] = formulario
        return render(request, 'producto/modificar_producto.html', data)
    else:
        return render(request,'acceso-denegado.html')    


#--------------------------Proveedores-----------------------------------------------------

def listar_proveedor(request):
    busqueda = request.GET.get("buscar")
    proveedores = Proveedor.objects.all()
    if busqueda:
        proveedores = Proveedor.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(rut__icontains = busqueda)
        ).distinct()
    if request.user.is_staff:    
        return render(request, 'proveedor/listaProveedores.html', {'entity':proveedores})
    else:
         return render(request,'acceso-denegado.html')    


# def listar_categoria(request):
#     busqueda = request.GET.get("buscar")
#     categorias = Categoria.objects.all()
#     if busqueda:
#         categorias = Categoria.objects.filter(
#             Q(descripcion__icontains = busqueda)  
#         ).distinct()
#     return render(request, 'categoria/listaCategorias.html', {'entity':categorias})


def agregar_proveedor(request):
    if request.user.is_staff: 
        data = {
            'form' : ProveedorForm()
        }
        if request.method == 'POST':
            formulario = ProveedorForm(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Proveedor Creado correctamente")
                return redirect(to="proveedores")
            data["form"] = formulario   
        return render(request, 'proveedor/agregar_proveedor.html', data)
    else:
        return render(request,'acceso-denegado.html') 
            

def eliminar_proveedor(request, id):
    if request.user.is_staff: 
        proveedor = get_object_or_404(Proveedor, id_proveedor=id)
        proveedor.delete()
        messages.success(request, "Eliminado correctamente")
        return redirect(to="proveedores")
    else:
        return render(request,'acceso-denegado.html')     


def modificar_proveedor(request, id): 
    if request.user.is_staff: 
        proveedor = get_object_or_404(Proveedor, id_proveedor=id)
        data = {
            'form': ProveedorEditForm(instance=proveedor)
        }
        if request.method == 'POST':
            formulario = ProveedorEditForm(data=request.POST, instance=proveedor)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "modificado correctamente")
                return redirect(to="proveedores")
            else:
                data["form"] = formulario
        return render(request, 'proveedor/modificar_proveedor.html', data)
    else:
        return render(request,'acceso-denegado.html')     

#--------------------------Categorias-----------------------------------------------------


def listar_categoria(request):
    busqueda = request.GET.get("buscar")
    categorias = Categoria.objects.all()
    if busqueda:
        categorias = Categoria.objects.filter(
            Q(descripcion__icontains = busqueda)  
        ).distinct()
    if request.user.is_staff: 
        return render(request, 'categoria/listaCategorias.html', {'entity':categorias})
    else:
        return render(request,'acceso-denegado.html')    

def agregar_categoria(request):
    if request.user.is_staff: 
        data = {
            'form' : CategoriaForm()
        }
        if request.method == 'POST':
            formulario = CategoriaForm(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Categoria creado correctamente")
                return redirect(to="categorias")
            data["form"] = formulario
        return render(request, 'categoria/agregar_categoria.html', data)
    else:
        return render(request,'acceso-denegado.html')    

def eliminar_categoria(request, id):
    if request.user.is_staff:
        if request.user.is_staff: 
            categoria = get_object_or_404(Categoria, id_categoria=id)
            categoria.delete()
            messages.success(request, "Eliminado correctamente")
            return redirect(to="categorias")
        else:
            return render(request,'acceso-denegado.html') 
    else:
        return render(request,'acceso-denegado.html')              


def modificar_categoria(request, id):
    if request.user.is_staff: 
        categorias = get_object_or_404(Categoria, id_categoria=id)
        data ={
            'form': CategoriaForm(instance=categorias)
        }
        if request.method == 'POST':
            formulario = CategoriaForm(data=request.POST, instance=categorias)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "modificado correctamente")
                return redirect(to="categorias")
            data["form"] = formulario
        return render(request, 'categoria/modificar_categoria.html', data)
    else:
        return render(request,'acceso-denegado.html')         