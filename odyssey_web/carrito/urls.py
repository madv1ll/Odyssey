from django.urls import path
from .import views
from .views import CarritoView, DetalleCompra

app_name = "carrito"


urlpatterns = [

    
    path("agregar/<int:producto_id>/", views.agre_producto, name="agregar_carro"),
    path("sumar/<int:producto_id>/", views.sumar_producto, name="sumar_carro"),
    path('restar/<int:producto_id>/', views.restar_producto, name = "restar_carro"),
    path('limpiar/', views.limpiar_carro, name = "limpiar"),
    path('', CarritoView.as_view(), name='carrito_view'),
    # path('carrito/', carrito , name= "carrito"),
    path('confirmacion/', DetalleCompra.as_view() , name= "confirmacion"),
]