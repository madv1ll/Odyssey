from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import login, logout


from .models import  Direccion, Usuario
from .forms import UsuarioForm, DireccionForm
from carrito.models import Compra, Detalle_compra
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
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
    success_url = reverse_lazy('home')

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
    busqueda = request.GET.get("buscar")
    u = Usuario.objects.all()
    if busqueda:
        u = Usuario.objects.filter(
            Q(username__icontains = busqueda) 
        ).distinct()

    return render(request, 'user/listaUsuarios.html', {'entity':u})     



def eliminar(request, id):
    user = get_object_or_404(Usuario, rut = id)
    user.delete()
    messages.success(request, "eliminado correctamente")
    return redirect(to="users")


def modificar_usuario(request, id):
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
        form = DireccionForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.id_usuario = Usuario.objects.only('rut').get(rut=id)
            post.save()
            return redirect (to="home")
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
    if request.method == 'POST':
        formulario = DireccionForm(data=request.POST, instance=direccion, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            # messages.success(request, "modificado correctamente")
            return redirect(to="home")
        else:
            data["form"] = formulario
    return render(request, 'perfil/direccion/editar_direccion.html', data)

def eliminar_direccion(request, id):
    direccion = get_object_or_404(Direccion, id_direccion=id)
    direccion.delete()
    messages.success(request, "eliminado correctamente")
    return redirect(to="home")


def lista_detalleCompra(request, id):
    compra = Compra.objects.filter(rut_usuario=id)
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
						send_mail(subject, email, 'odyssseygamming@gmail.com' , [user.correo], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="resetPassword/password_reset.html", context={"password_reset_form":password_reset_form})