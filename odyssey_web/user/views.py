from email import message
from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
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
    u = User.objects.all()
    data = {
        'entity': u,
    }
    return render(request, 'user/listaUsuarios.html', data)     


