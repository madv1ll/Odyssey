from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import registro, users, eliminar, modificar_usuario

urlpatterns = [
    path('registro/', registro, name="registro"),
    path('login/', LoginView.as_view(template_name = 'login/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'web/home.html'), name='logout'),
    #administrar usuarios
    path('users/', users, name="users"),
    path('eliminar_usuario/<id>/', eliminar, name="eliminar_user"),
    path('modificar_usuario/<id>/', modificar_usuario, name="modificar_usuario"),

]
