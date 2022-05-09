from django.shortcuts import get_object_or_404, render
from .carro import Carro
from producto.models import Producto
from user.models import Usuario
from .models import  Detalle_compra
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
        amount = total
        buy_order="1"
        session_id="1"
        return_url= 'http://localhost:8000/carrito/confirmacion/'

        tx = Transaction(WebpayOptions(IntegrationCommerceCodes.WEBPAY_PLUS,
        IntegrationApiKeys.WEBPAY,
        IntegrationType.TEST))
        resp = tx.create(buy_order, session_id, amount, return_url)
        # print(resp)
        return render(request,"carro/confirmacion.html",{"resp":resp})

 
class DetalleCompra(View):
    def get(self,request,*args,**kwargs):
        token = request.GET.get("token_ws")
        tx = Transaction(WebpayOptions(IntegrationCommerceCodes.WEBPAY_PLUS, IntegrationApiKeys.WEBPAY, IntegrationType.TEST))
        success = tx.commit(token)
        # print(success)
        if success.get("status") == "AUTHORIZED":
            if request.user.is_active:
                cliente = request.user.rut
            else:
                cliente = "99.999.999-K"
            total = 0
            obj_cliente = Usuario.objects.only('rut').get(rut=cliente)
            for key, value in request.session["carro"].items():
                total=total+(float(value["precio"]))
                # creacion del registro del producto
                registro = ""
                registro = Detalle_compra(
                    id_producto     = value["producto_id"],
                    rut_cliente     = obj_cliente,
                    precio_producto = value["precio"],
                    cantidad        = value["cantidad"]
                )
                registro.save()

            Carro.limpiar_carro(request)
        else:
            # print("rechazado")
            registro = "no crear registro"
        return render(request,"carro/confirmacion.html",{"success":success})

	# DEBITO = 4051 8842 3993 7763
    # 11 111 111 1
    # 123

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