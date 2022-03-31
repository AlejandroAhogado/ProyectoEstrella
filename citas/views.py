from .logic import citas_logic as cl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def citas_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            cita_dto = cl.get_cita(id)
            cita = serializers.serialize('json', [cita_dto,])
            return HttpResponse(cita, 'application/json')
        else:
            citas_dto = cl.get_citas()
            citas = serializers.serialize('json', citas_dto)
            return HttpResponse(citas, 'application/json')

    if request.method == 'POST':
        cita_dto = cl.create_cita(json.loads(request.body))
        cita = serializers.serialize('json', [cita_dto,])
        return HttpResponse(cita, 'application/json')


@csrf_exempt
def cita_view(request, pk):
    if request.method == 'GET':
        cita_dto = cl.get_cita(pk)
        cita = serializers.serialize('json', [cita_dto, ])
        return HttpResponse(cita, 'application/json')

    if request.method == 'PUT':
        cita_dto = cl.update_cita(pk, json.loads(request.body))
        cita = serializers.serialize('json', [cita_dto, ])
        return HttpResponse(cita, 'application/json')

    if request.method == 'DELETE':
        cita_dto = cl.delete_cita(pk)
        cita = serializers.serialize('json', [cita_dto, ])
        return HttpResponse(cita, 'application/json')