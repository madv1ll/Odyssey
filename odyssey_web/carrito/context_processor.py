from administrador.models import PrecioEnvio


def importe_total_carro(request):
    total=0
    if 'carro' in request.session:
        for key, value in request.session["carro"].items():
            total=total+(int(value["precio"]))
    return {"importe_total_carro":total}


def precio_totalMasEnvio(request):
    precio_envio = PrecioEnvio.objects.only('precio').get(id_envio=1)
    total=0
    if 'carro' in request.session:
        for key, value in request.session["carro"].items():
            total=total+(int(value["precio"])+ precio_envio.precio)
    return {"precio_totalMasEnvio":total}    