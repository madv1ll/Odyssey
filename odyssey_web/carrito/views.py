from django.shortcuts import render
from .carro import Carro
from producto.models import Producto
from .models import Detalle_compra
from django.shortcuts import  redirect
from django.views.generic.edit import CreateView
from django.views.generic import View
from carrito.models import Detalle_compra
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.views.generic import View
#transbank
from transbank.webpay.webpay_plus.transaction import Transaction
from transbank.common.options import WebpayOptions
from transbank.common.integration_commerce_codes import IntegrationCommerceCodes
from transbank.common.integration_api_keys import IntegrationApiKeys
from transbank.common.integration_type import IntegrationType
from carrito.context_processor import importe_total_carro

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

def ConfirmacionCompra(request):
    return render(request, 'carro/confirmacion.html')

class CarritoView(View):

    def get(self,request,*args,**kwargs): 
        
        return render(request, 'carro/carrito.html')

    def post(self,request,*args,**kwargs):
        total = 0
        for key, value in request.session["carro"].items():
            total=total+(float(value["precio"]))
        print(request.session["carro"].items())
        amount = total
        buy_order="1"
        session_id="1"
        return_url= 'http://localhost:8000/carrito/confirmacion/'

        tx = Transaction(WebpayOptions(IntegrationCommerceCodes.WEBPAY_PLUS,
        IntegrationApiKeys.WEBPAY,
        IntegrationType.TEST))
        resp = tx.create(buy_order, session_id, amount, return_url)
        print(resp)
        return render(request,"carro/confirmacion.html",{"resp":resp})

 
class DetalleCompra(View):
    def get(self,request,*args,**kwargs):
        token = request.GET.get("token_ws")
        tx = Transaction(WebpayOptions(IntegrationCommerceCodes.WEBPAY_PLUS, IntegrationApiKeys.WEBPAY, IntegrationType.TEST))
        success = tx.commit(token)
        print(success)
        return render(request,"carro/confirmacion.html",{"success":success})
	

# {'vci': 'TSY',
#  'amount': 99000, 
#  'status': 'AUTHORIZED', 
#  'buy_order': '1', 
#  'session_id': '1', 
#  'card_detail': {'card_number': '7763'}, 
#  'accounting_date': '0503', 
#  'transaction_date': '2022-05-03T05:51:28.484Z', 
#  'authorization_code': '1415', 
#  'payment_type_code': 'VD', 
#  'response_code': 0, 
#  'installments_number': 0}

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