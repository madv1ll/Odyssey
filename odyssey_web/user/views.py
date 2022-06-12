from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import login, logout
from requests import request

from web.models import Comuna
from .models import  Direccion, Usuario
from .forms import UsuarioForm, DireccionForm, UsuarioAdminForm
from carrito.models import Compra, Detalle_compra
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect, JsonResponse
from .forms import LoginForm
from django.contrib.auth.forms import PasswordResetForm
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

class RegistroView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    success_url = reverse_lazy('registro_completado')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if len(Usuario.objects.all()) == 0:
            context["primer_usuario"] = True
        return context

def registro_compleado(request):
    return render(request, 'register/completado.html')
    
class RegistroAdminView(CreateView):
    model = Usuario
    form_class = UsuarioAdminForm
    success_url = reverse_lazy('users')  
      
class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)
    def form_invalid(self,form):
        correo = form.cleaned_data['username']
        try: 
            user = Usuario.objects.get(username=correo)
        except:
            return super(LoginView, self).form_invalid(form)
        if  user.is_active == 0 or user.is_active == False:
            return  HttpResponseRedirect('/user/confirmar/')

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')

def my_view(request):
    if not request.user.is_authenticated:
        return render(request, 'myapp/login_error.html')
#-----------------------------
def users(request):
    if request.user.is_staff: 
        busqueda = request.GET.get("buscar")
        u = Usuario.objects.all()
        if busqueda:
            u = Usuario.objects.filter(
                Q(username__icontains = busqueda) |
                Q(rut__icontains = busqueda)
            ).distinct()

        return render(request, 'user/listaUsuarios.html', {'entity':u})     
    else:
        return render(request,'acceso-denegado.html')     

def eliminar(request, id):
    if request.user.is_staff: 
        user = get_object_or_404(Usuario, rut = id)
        user.delete()
        messages.success(request, "eliminado correctamente")
        return redirect(to="users")
    else:
        return render(request,'acceso-denegado.html')    


def modificar_usuario(request, id):
    if request.user.is_staff: 
        user = get_object_or_404(Usuario, rut=id)
        data = {
            'form': UsuarioForm(instance=user)
        }
        if request.method == 'POST':
            formulario = UsuarioForm(data=request.POST, instance=user, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "modificado correctamente")
                return redirect(to="users")
            else:
                data["form"] = formulario
        return render(request, 'user/modificar_usuario.html', data)
    else:
        return render(request,'acceso-denegado.html')    

#-------------Perfil de cliente--------------------------------------------

def listar_perfil(request, id):
    usuario = Usuario.objects.filter(rut=id)
    data = {
        'usuario':usuario
    }
    return render(request,'perfil/listarPerfil.html',data)


def modificar_perfil(request, id):
    user = get_object_or_404(Usuario, rut=id)
    data = {
        'form': UsuarioForm(instance=user)
    }
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, instance=user, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "modificado correctamente")
            return redirect(to="home")
        else:
            data["form"] = formulario
    return render(request, 'perfil/editarInfo.html', data)
    

def nueva_direccion(request, id):
    if request.method == "POST":
        try:
            
            action = str(request.POST['action'])
            if str(action) == 'buscar_comuna':
                data = []
                for i in  Comuna.objects.filter(id_region= request.POST['id']):
                    data.append({'comuna': i.id_comuna ,'nombre': i.nombre})
                return JsonResponse(data, safe=False)
        except:
            form = DireccionForm(request.POST)
            
            if form.is_valid():
                #update de direccion principal
                if request.POST['principal'] == 'SI':
                    Direccion.objects.all().update(principal='NO')
                post = form.save(commit = False)
                post.id_usuario = Usuario.objects.only('rut').get(rut=id)
                post.id_comuna = Comuna.objects.get(id_comuna=request.POST['id_comuna'])
                post.calle = request.POST['calle']
                post.numero = request.POST['numero']
                post.save()
                return redirect(to="/user/listar_direccion/"+str(request.user.rut))
    else:
        form = DireccionForm
    return render(request, 'perfil/direccion/crear_direccion.html', {'form':form})


def listar_direccion(request, id):
    direccion = Direccion.objects.filter(id_usuario=id)
    data = {
        'direccion':direccion
    }
    return render(request,'perfil/direccion/listar_direccion.html',data)

def modificar_direccion(request, id):
    direccion = get_object_or_404(Direccion, id_direccion=id)
    data = {
        'form': DireccionForm(instance=direccion)
    }
    print(data)
    if request.method == 'POST': 
        formulario = DireccionForm(data=request.POST, instance=direccion, files=request.FILES)
        try:
            action = request.POST['action']
            if action == 'buscar_comuna':
                data = []
                for i in  Comuna.objects.filter(id_region= request.POST['id']):
                    data.append({'comuna': i.id_comuna ,'nombre': i.nombre})
                return JsonResponse(data, safe=False)
        except:
            if formulario.is_valid():
                #update de direccion principal
                if request.POST['principal'] == 'SI':
                    Direccion.objects.all().update(principal='NO')
                formulario.save()
                # messages.success(request, "modificado correctamente")
                return redirect(to="/user/listar_direccion/"+str(request.user.rut))
            else:
                data["form"] = formulario
    return render(request, 'perfil/direccion/editar_direccion.html', data)

def eliminar_direccion(request, id):
    direccion = get_object_or_404(Direccion, id_direccion=id)
    direccion.delete()
    messages.success(request, "eliminado correctamente")
    return redirect(to="/user/listar_direccion/"+str(request.user.rut))


def lista_detalleCompra(request, id):
    compra = Compra.objects.filter(rut_usuario=id).order_by('fecha').reverse()
    return render(request,'perfil/compra/detalle_compra.html', {'compra':compra})

def listar_productosCompraCLi(request, id):
    productosCompra = Detalle_compra.objects.filter( id_compra=id)
    return render(request, 'perfil/compra/productos.html', {'entity':productosCompra})

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = Usuario.objects.filter(Q(correo=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Reinicio de contraseña"
					email_template_name = "resetPassword/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'odysseygamming@outlook.com' , [user.correo], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="resetPassword/password_reset.html", context={"password_reset_form":password_reset_form})
###validacion emailll
def confirmacion_correo(request, token):
    # Verifica que el usuario ya está logeado
    if request.user.is_authenticated:
        HttpResponseRedirect('home')

    # Verifica que el token de activación sea válido y sino retorna un 404
    user_profile = get_object_or_404(Usuario, activation_key=token)

    # verifica si el token de activación ha expirado y si es así renderiza el html de registro expirado
    if user_profile.key_expires < timezone.now():
        return render(request, 'user/token_expirado.html')
    # Si el token no ha expirado, se activa el usuario y se muestra el html de confirmación
    user_profile.is_active = True
    user_profile.save()
    return render (request, 'user/confirmacion_correo.html')

def confirmar(request):
    return render(request, 'user/confirmar.html')