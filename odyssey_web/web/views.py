from importlib import import_module
from sre_constants import SUCCESS
from django.shortcuts import render
from producto.models import Producto
from django.core.paginator import Page, Paginator
from django.db.models import Q
from carrito.models import Detalle_compra
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.views.generic import View
from carrito.models import Carrito
from carrito.utils import get_or_create_carrito
#transbank
from transbank.webpay.webpay_plus.transaction import Transaction
from transbank.common.options import WebpayOptions
from transbank.common.integration_commerce_codes import IntegrationCommerceCodes
from transbank.common.integration_api_keys import IntegrationApiKeys
from transbank.common.integration_type import IntegrationType
from carrito.context_processor import importe_total_carro




def home(request):
    return render(request, 'web/home.html')

def listar_productosVenta(request):
    busqueda = request.GET.get("buscar")
    productos = Producto.objects.filter(stock__gt=0)
    if busqueda:
        productos = Producto.objects.filter(
             stock__gt=0 and
            Q(nombre__icontains = busqueda) |
            Q(descripcion__icontains = busqueda)
        ).distinct()
    return render(request, 'web/productos.html', {'entity':productos})
  

def ConfirmacionCompra(request):
    return render(request, 'carro/confirmacion.html')


class CarritoView(View):

    def get(self,request,*args,**kwargs): 
        
        carrito = get_or_create_carrito(request)

        return render(request, 'carro/carrito.html',{
            'carrito':carrito
        })


    def post(self,request,*args,**kwargs):
        buy_order="1"
        session_id="1"
        amount = 99000
        return_url= 'http://127.0.0.1:8000/confirmacion/'

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