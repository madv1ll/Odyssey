from msilib.schema import Media
from tkinter.ttk import Style
from django.conf import settings
from django.shortcuts import get_object_or_404, render

from user.models import Direccion
from .carro import Carro
from producto.models import Producto
from user.models import Usuario
from .models import  Compra, Detalle_compra, Tipo_Pago
from django.shortcuts import  redirect
from django.views.generic.edit import CreateView
from django.views.generic import View
from carrito.models import Detalle_compra
from administrador.models import PrecioEnvio
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

#send mail
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string

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
    return redirect("/carrito")    

def restar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id_producto =producto_id)
    carro.restar_producto(producto= producto)
    return redirect("/carrito")

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
        envio = PrecioEnvio.objects.all()
        precio_envio = PrecioEnvio.objects.only('precio').get(id_envio=1)
        total = 0 + precio_envio.precio
        for key, value in request.session["carro"].items():
            total=total+(float(value["precio"])) 
            print(total)
        amount = total
        buy_order="1"
        session_id="1"
        cliente = request.user.rut   
        return_url= 'http://127.0.0.1:8000/carrito/confirmacion/'+str(cliente)+'/'
        direccion_clie = Direccion.objects.filter(id_usuario = cliente).filter(principal="SI")
        tx = Transaction(WebpayOptions(IntegrationCommerceCodes.WEBPAY_PLUS,
        IntegrationApiKeys.WEBPAY,
        IntegrationType.TEST))
        resp = tx.create(buy_order, session_id, amount, return_url)
        return render(request,"carro/confirmacion.html",{"resp":resp, "direccion":direccion_clie, "precio_envio":envio})

 
class DetalleCompra(View):
    def get(self,request,rut,*args,**kwargs):
        print(request)
        token = request.GET.get("token_ws")
        tx = Transaction(WebpayOptions(IntegrationCommerceCodes.WEBPAY_PLUS, IntegrationApiKeys.WEBPAY, IntegrationType.TEST))
        success = tx.commit(token)
        if success.get("status") == "AUTHORIZED":
            total = 0
            obj_cliente = Usuario.objects.only('rut').get(rut=rut)
            tpo_pago = Tipo_Pago.objects.only('id_tipo_pago').get(id_tipo_pago=success.get('payment_type_code'))
            direc= Direccion.objects.only("id_direccion").filter(principal="SI").get(id_usuario=rut)
            compra = Compra(
                    rut_usuario =  obj_cliente,
                    id_tipo_pago = tpo_pago,
                    id_direccion = direc,
                    total = success.get('amount')
            )
            compra.save()
            for key, value in request.session["carro"].items():
                total=total+(float(value["precio"]))
                # creacion del registro del producto
                prod = Producto.objects.only('id_producto').get(id_producto=value["producto_id"])
                registro = Detalle_compra(
                    id_producto     = prod,
                    rut_cliente     = obj_cliente,
                    precio_producto = value["precio"],
                    cantidad        = value["cantidad"],
                    id_compra       = Compra.objects.latest("fecha")
                )
                registro.save()
            Carro.limpiar_carro(request)
            #send mail
            correoUsuario = request.user.correo
            subject = "Compra realizada con ??xito!"
            email_template_name =  "carro/email/emailConfirm.txt"
            message = render_to_string(email_template_name)		
            send_mail(subject, message, 'odysseygamming@outlook.com',[correoUsuario], fail_silently=False)
        else:
            # print("rechazado")
            registro = "no crear registro"
        return render(request,"carro/confirmacion.html",{"success":success})