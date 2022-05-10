from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.db.models import Q
from django.contrib import messages

from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

from django.contrib.auth import login, logout
from .models import  Usuario
from .forms import UsuarioForm
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from .forms import LoginForm

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


def send_email(mail):
    print ('se envio el correo')
    context = {'mail': mail}

    template = get_template('password_reset_email.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Un correo de prueba',
        settings.EMAIL_HOST_USER,
        [mail]
    )

    email.attach_alternative(content, 'text/html')
    email.send()




# class RecuperarContra(View):
#     def password_reset(request):
#     print ('se recibe correo')
#     if request.method == 'POST':
        
#         mail = request.POST.get('mail')

#         send_email(mail)

#     return render(request, 'recuperarcontra/password_reset.html', {})