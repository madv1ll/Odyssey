from django.urls import include, path
from .views import administrador

urlpatterns = [
    path('', administrador, name="administrador"),
]
