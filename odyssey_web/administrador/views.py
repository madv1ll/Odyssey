from django.shortcuts import render

def administrador(request):
    return render(request, 'admin.html')


