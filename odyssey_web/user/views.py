from email import message
from email.headerregistry import Group
from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .forms import  CustomUserCreationForm
from django.contrib.auth import authenticate, forms, login
from django.contrib import messages
from django.contrib.auth.models import User



# Create your views here.

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])            
            login(request, user)
            messages.success(request, "Te has registrado correctamente ")
            return redirect(to="home")
        data["form"] = formulario
    return render(request, 'login/registro.html', data)


#administrar usuarios

def users(request):
    busqueda = request.GET.get("buscar")
    u = User.objects.filter(is_staff = 0)
    if busqueda:
        u = User.objects.filter(
            Q(username__icontains = busqueda) 
        ).distinct()

    return render(request, 'user/listaUsuarios.html', {'entity':u})     



def eliminar(request, id):
    user = get_object_or_404(User, id = id)
    user.delete()
    messages.success(request, "eliminado correctamente")
    return redirect(to="users")


def modificar_usuario(request, id):
    user = get_object_or_404(User, id=id)
    data = {
        'form': CustomUserCreationForm(instance=user)
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST, instance=user, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "modificado correctamente")
            return redirect(to="users")
        else:
            data["form"] = formulario
    return render(request, 'user/modificar_usuario.html', data)