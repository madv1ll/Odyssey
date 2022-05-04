from django.shortcuts import render
from .carro import Carro
from producto.models import Producto
from .models import Detalle_compra
from django.shortcuts import  redirect
from django.views.generic.edit import CreateView

# Create your views here.
def agre_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id_producto = producto_id)
    carro.agregar(producto = producto)
    return redirect("productosVenta")

def sumar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id_producto = producto_id)
    carro.agregar(producto = producto)
    return redirect("carrito")    


def restar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id_producto =producto_id)
    carro.restar_producto(producto= producto)
    return redirect("carrito")


def limpiar_carro(request):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect("carrito")  



# ## detalle de compra
# class DetalleCompra_Crear(CreateView): 
#     model = Detalle_compra # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
#     form = Detalle_compra # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres'
#     fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
#     # Redireccionamos a la página principal luego de crear un registro o postre
#     def get_success_url(self, request):        
#         return render(request, 'web/agregar_proveedor.html')


# def detalle_compra(request):
#     return render('')