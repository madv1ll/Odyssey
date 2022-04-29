# from email import message
# from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
# from .forms import  CustomUserCreationForm 
from django.views.generic import CreateView
from django.contrib.auth import authenticate, forms, login
#import Q  para busqueda 
from django.db.models import Q
from django.contrib import messages

from django.contrib.auth.models import User
from .models import  Usuario

from .forms import UsuarioForm

class RegistroView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    success_url = reverse_lazy('home')
#-----------------------------

def users(request):
    busqueda = request.GET.get("buscar")
    u = User.objects.filter(is_staff = 0)
    if busqueda:
        u = User.objects.filter(
            Q(username__icontains = busqueda) 
        ).distinct()

    return render(request, 'user/listaUsuarios.html', {'entity':u})     



def eliminar(request, id):
    user = get_object_or_404(Usuario, id = id)
    user.delete()
    messages.success(request, "eliminado correctamente")
    return redirect(to="users")


# def modificar_usuario(request, id):
#     user = get_object_or_404(User, id=id)
#     data = {
#         'form': CustomUserCreationForm(instance=user)
#     }
#     if request.method == 'POST':
#         formulario = CustomUserCreationForm(data=request.POST, instance=user, files=request.FILES)
#         if formulario.is_valid():
#             formulario.save()
#             messages.success(request, "modificado correctamente")
#             return redirect(to="users")
#         else:
#             data["form"] = formulario
#     return render(request, 'user/modificar_usuario.html', data)