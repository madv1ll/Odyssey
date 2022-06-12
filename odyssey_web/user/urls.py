from django.urls import path
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from .views import LoginView, RegistroView, RegistroAdminView, confirmacion_correo, confirmar, modificar_usuario, registro_compleado, users, eliminar, \
 modificar_perfil, listar_perfil, listar_direccion, nueva_direccion, \
modificar_direccion, eliminar_direccion, lista_detalleCompra, listar_productosCompraCLi, password_reset_request


urlpatterns = [
    path('registro/', RegistroView.as_view(template_name = 'register/user_form.html'), name="registro"),
    path('registro_admin', RegistroAdminView.as_view(template_name = 'register/user_adminForm.html'), name="registro_admin"),
    path('login/', LoginView.as_view(template_name = 'login/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'web/home.html'), name='logout'),
    # path('registro/completado', RegistroView.as_view(template_name = 'register/completado.html'), name="registro_completado"),
    path('registro/completado', registro_compleado, name="registro_completado"),
    
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
    path('producto_compra/<id>/',listar_productosCompraCLi, name='producto_compra'),
    #recuperar contraseña
    path("password_reset", password_reset_request, name="password_reset"),
    #path('reset_password/', PasswordResetView.as_view(template_name = 'resetPassword/password_reset_form.html'), name ="password_reset"), 
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='resetPassword/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="resetPassword/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='resetPassword/password_reset_complete.html'), name='password_reset_complete'),  
    #confirmacion correo
    path('confirmacion/<str:token>/', confirmacion_correo, name='confirmacion_correo'),
    path('confirmar/', confirmar, name='confirmar'),
]