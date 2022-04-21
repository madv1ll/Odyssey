from django.shortcuts import render

def home(request):
    return render(request, 'web/home.html')

def administrador(request):
    return render(request, 'administrador/admin.html')