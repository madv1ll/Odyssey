from django.urls import path
from .import views

app_name = "carrito"


urlpatterns = [

    # path("agregar/<int:producto_id>/", views.agre_producto, name="agregar_carro"),
    path('agregar', views.agre_producto,name="agregar_carro"),
    path('eliminar', views.remove,name="remove"),
    path("sumar/<int:producto_id>/", views.sumar_producto, name="sumar_carro"),
    path('restar/<int:producto_id>/', views.restar_producto, name = "restar_carro"),
    path('limpiar/', views.limpiar_carro, name = "limpiar"),
]