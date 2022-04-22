
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from .forms import CategoriaForm, ProductoForm, ProveedorForm
from .models import Proveedor, Categoria, Producto
from django.contrib import messages


def listar_productos(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': productos,
        'paginator': paginator
    }
    return render(request, 'producto/listaProducto.html', data)

def agregar_producto(request):
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

def eliminar_producto(request, id): 
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "eleiminado correctamente")
    return redirect(to="listar_productos")    

def modificar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    data = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "modificado correctamente")
            return redirect(to="listar_productos")
        else:
            data["form"] = formulario
    return render(request, 'administrador/producto/modificar_producto.html', data)

# Proveedores
def listar_proveedor(request):
    proveedores = Proveedor.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(proveedores, 5)
        proveedores = paginator.page(page)
    except:
        raise Http404   
    data = {
        'entity': proveedores,
        'paginator': paginator
    }
    return render(request, 'proveedor/listaProveedores.html', data)

def agregar_proveedor(request):
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

def eliminar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id_proveedor=id)
    proveedor.delete()
    messages.success(request, "eleiminado correctamente")
    return redirect(to="proveedores")

def modificar_proveedor(request, id): 
    proveedor = get_object_or_404(Proveedor, id_proveedor=id)
    data = {
        'form': ProveedorForm(instance=proveedor)
    }
    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST, instance=proveedor)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "modificado correctamente")
            return redirect(to="proveedores")
        else:
            data["form"] = formulario
    return render(request, 'proveedor/modificar_proveedor.html', data)

def listar_categoria(request):
    categorias = Categoria.objects.all()
    page = request.GET.get('page',1)
    try:
        paginator = Paginator(categorias, 5)
        categorias = paginator.page(page)
    except:
        raise Http404
    data = {
        'entity': categorias,
        'paginator': paginator
    }
    return render(request, 'categoria/listaCategorias.html', data)

def agregar_categoria(request):
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

def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    messages.success(request, "eliminado correctamente")
    return redirect(to="categorias")

def modificar_categoria(request, id):
    categorias = get_object_or_404(Categoria, id=id)
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