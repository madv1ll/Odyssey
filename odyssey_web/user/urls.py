from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import registro, users

urlpatterns = [
    path('registro/', registro, name="registro"),
    path('login/', LoginView.as_view(template_name = 'login/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'web/home.html'), name='logout'),
    #administrar usuarios
    path('users/', users, name="users"),

]
