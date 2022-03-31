from ..models import Cita
from ..models import Tutor


def get_citas():
    citas = Cita.objects.all()
    return citas


def get_cita(var_pk):
    cita = Cita.objects.get(pk=var_pk)
    return cita


#Revisar porque no se los atributos de cita, esta mal
def update_cita(var_pk, new_var):
    cita = get_cita(var_pk)
    cita.horario = new_var["horario"]
    cita.save()
    return cita


def create_cita(var):
    tutor = Tutor.objects.get(pk=var["tutor"])
    cita = Cita(tutor=tutor,
                horario=var["horario"])
    cita.save()
    return cita


def delete_cita(var_pk):
    #Measurement.objects.filter(pk=var_pk).delete()
    cita = get_cita(var_pk)
    #measurement = Measurement.objects.get(pk=var_pk)
    cita.delete()
    return HttpResponse()