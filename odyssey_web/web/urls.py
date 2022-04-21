from django.urls import include, path
from .views import home, administrador

urlpatterns = [
    path('', home, name="home"),
    path('administrador/', administrador, name="administrador"),
]
