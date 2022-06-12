
from django.shortcuts import get_object_or_404, redirect, render
from carrito.models import Compra, Detalle_compra
from .forms import CompraEditForm, PrecioEnvioEditForm
from django.contrib import messages
from .models import PrecioEnvio
from user.models import Usuario
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError

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
        compra = get_object_or_404(Compra, id_compra=id)
        
        data = {
            'form': CompraEditForm(instance=compra)
        }
        if request.method == 'POST':
            formulario = CompraEditForm(data=request.POST, instance=compra, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "modificado correctamente")
                estado = compra.estado
                correoUsuario = compra.rut_usuario.correo
                nombreUsuario = compra.rut_usuario.nombre
                telefonoUsuario = compra.rut_usuario.telefono

                if estado == 'Pedido en camino':
                    correoUsuario = correoUsuario
                    subject = "Cambio de estado de tu compra"
                    email_template_name =  "estadoCompra/enviado.txt"
                    c = {
                        "nombre": nombreUsuario,
                        "telefono": telefonoUsuario
                    }
                    message = render_to_string(email_template_name, c)		
                    send_mail(subject, message, 'odysseygamming@outlook.com',[correoUsuario], fail_silently=False)

                elif(estado == 'Pedido entregado'):
                    correoUsuario = correoUsuario
                    subject = "Cambio de estado de tu compra"
                    email_template_name =  "estadoCompra/entregado.txt"
                    c = {
                        "nombre": nombreUsuario,
                        "telefono": telefonoUsuario
                    }
                    message = render_to_string(email_template_name, c)		
                    send_mail(subject, message, 'odysseygamming@outlook.com',[correoUsuario], fail_silently=False)   

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