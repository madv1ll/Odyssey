from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import LoginView, RegistroView, modificar_usuario, users, eliminar, modificar_perfil, listar_perfil
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registro/', RegistroView.as_view(template_name = 'register/user_form.html'), name="registro"),
    path('login/', LoginView.as_view(template_name = 'login/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'web/home.html'), name='logout'),
    #administrar usuarios
    path('users/', users, name="users"),
    path('eliminar_usuario/<id>/', eliminar, name="eliminar_user"),
    path('modificar_usuario/<id>/', modificar_usuario, name="modificar_usuario"),
    path('modificar_perfil/<id>/', modificar_perfil, name='modificar_perfil'),
    path('listarPerfil/<id>/', listar_perfil, name='listar_perfil'),

]