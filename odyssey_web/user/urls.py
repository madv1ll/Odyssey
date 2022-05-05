from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import LoginView, RegistroView, users, eliminar, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('registro/', RegistroView.as_view(template_name = 'register/user_form.html'), name="registro"),
    path('login/', LoginView.as_view(template_name = 'login/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'web/home.html'), name='logout'),
    #administrar usuarios
    path('users/', users, name="users"),
    path('eliminar_usuario/<id>/', eliminar, name="eliminar_user"),
    # path('modificar_usuario/<id>/', modificar_usuario, name="modificar_usuario"),
    path('password_reset', PasswordResetView.as_view(), name="password_reset"),
    path('password_reset_done', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/done', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    #recuperar contraseña
]