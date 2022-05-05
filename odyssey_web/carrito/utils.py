from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
from .models import Carrito


def get_or_create_carrito(request):
    user = request.user if request.user.is_authenticated else None
    carro_id = request.session.get('carro_id') 
    carrito = Carrito.objects.filter(carro_id=carro_id).first()

    if carrito is None:
        carrito = Carrito.objects.create(user=user)
        
    if user and carrito.user is None:
        carrito.user = user
        carrito.save()

    request.session['carro_id'] = carrito.carro_id 

    return carrito