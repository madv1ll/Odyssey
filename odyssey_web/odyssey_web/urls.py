from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls')),
    # producto
    path('productos/', include('producto.urls')),
    #admin
    path('administrador/',include('administrador.urls')),
    #user
    path('user/',include('user.urls')),
    #carrito
    path('carrito/',include('carrito.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)