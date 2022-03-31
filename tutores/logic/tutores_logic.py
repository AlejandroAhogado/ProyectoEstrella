from ..models import Tutor

def get_tutores():
    tutores = Tutor.objects.all()
    return tutores

def get_tutor(var_pk):
    tutor = Tutor.objects.get(pk=var_pk)
    return tutor

def update_tutor(var_pk, new_var):
    tutor = get_tutor(var_pk)
    tutor.name = new_var["name"]
    tutor.save()
    return tutor

def create_tutor(var):
    tutor = Tutor(nombre=var["name"],
                  correo=var["correo"])
    tutor.save()
    return tutor