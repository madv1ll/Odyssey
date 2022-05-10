from django.urls import path
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .views import LoginView, RegistroView, modificar_usuario, users, eliminar, password_reset

urlpatterns = [
    path('registro/', RegistroView.as_view(template_name = 'register/user_form.html'), name="registro"),
    path('login/', LoginView.as_view(template_name = 'login/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'web/home.html'), name='logout'),
    #administrar usuarios
    path('users/', users, name="users"),
    path('eliminar_usuario/<id>/', eliminar, name="eliminar_user"),
    # path('modificar_usuario/<id>/', modificar_usuario, name="modificar_usuario"),
    #recuperar contraseña
    path('password_reset/', PasswordResetView.as_view(template_name = 'recuperarcontra/password_reset.html'), name='password_reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(template_name = 'recuperarcontra/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/', PasswordResetConfirmView.as_view(template_name = 'recuperarcontra/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(template_name = 'recuperarcontra/password_reset_complete.html'), name='password_reset'),
    

    path('modificar_usuario/<id>/', modificar_usuario, name="modificar_usuario"),
]