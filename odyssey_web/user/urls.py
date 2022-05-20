from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import LoginView, RegistroView, modificar_usuario, users, eliminar, \
 modificar_perfil, listar_perfil, listar_direccion, nueva_direccion, \
modificar_direccion, eliminar_direccion, lista_detalleCompra, listar_productosCompraCLi


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
    #direcciones
    path('nueva_direccion/<id>/',nueva_direccion, name='nueva_direccion'),
    path('listar_direccion/<id>/',listar_direccion, name='listar_direccion'),
    path('modificar_direccion/<id>/',modificar_direccion, name='modificar_direccion'),
    path('eliminar_direccion/<id>/',eliminar_direccion, name='eliminar_direccion'),
    #detalle_compras
    path('detalle_compra/<id>/',lista_detalleCompra, name='lista_detalleCompra'),
    path('producto_compra/<id>/',listar_productosCompraCLi, name='producto_compra')

]