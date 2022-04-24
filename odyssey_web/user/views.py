# from email import message
# from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
# from .forms import  CustomUserCreationForm
from django.views.generic import CreateView
from django.contrib.auth import authenticate, forms, login
# from django.contrib import messages

from django.contrib.auth.models import User
from .models import Perfil

from .forms import SignUpForm

# def registro(request):
#     data = {
#         'form': CustomUserCreationForm()
#     }
#     if request.method == 'POST':
#         formulario = CustomUserCreationForm(data=request.POST)
#         if formulario.is_valid():
#             formulario.save()
#             user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])            
#             login(request, user)
#             messages.success(request, "Te has registrado correctamente ")
#             return redirect(to="home")
#         data["form"] = formulario
#     return render(request, 'login/registro.html', data)

class RegistroView(CreateView):
    model = Perfil
    form_class = SignUpForm

    def form_valid(self, form):
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')
#administrar usuarios

def users(request):
    u = User.objects.all()
    data = {
        'entity': u,
    }
    return render(request, 'user/listaUsuarios.html', data)     


