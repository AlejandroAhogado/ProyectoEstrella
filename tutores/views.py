from .logic import tutores_logic as tl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def tutores_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            tutor_dto = tl.get_tutor(id)
            tutor = serializers.serialize('json', [tutor_dto,])
            return HttpResponse(tutor, 'application/json')
        else:
            tutores_dto = tl.get_tutores()
            tutores = serializers.serialize('json', tutores_dto)
            return HttpResponse(tutores, 'application/json')

    if request.method == 'POST':
        tutor_dto = tl.create_tutor(json.loads(request.body))
        tutor = serializers.serialize('json', [tutor_dto,])
        return HttpResponse(tutor, 'application/json')


@csrf_exempt
def tutor_view(request, pk):
    if request.method == 'GET':
        tutor_dto = tl.get_tutor(pk)
        tutor = serializers.serialize('json', [tutor_dto, ])
        return HttpResponse(tutor, 'application/json')

    if request.method == 'PUT':
        tutor_dto = tl.update_variable(pk, json.loads(request.body))
        tutor = serializers.serialize('json', [tutor_dto, ])
        return HttpResponse(tutor, 'application/json')


# def variables_view(request):
#     if request.method == 'GET':
#         variables = vl.get_variables()
#         variables_dto = serializers.serialize('json', variables)
#         return HttpResponse(variables_dto, 'application/json')

# def variable_view(request, pk):
#     if request.method == 'GET':
#         variable = vl.get_variable(pk)
#         variable_dto = serializers.serialize('json', variable)
#         return HttpResponse(variable_dto, 'application/json')
