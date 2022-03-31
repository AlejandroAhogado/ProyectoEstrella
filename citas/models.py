from django.db import models

from tutores.models import Tutor
# Create your models here.
class Cita(models.Model):
    horario = models.DateTimeField(auto_now_add=True)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, default=None)

    def __str__(self):

        return '{} {}'.format(self.tutor, self.horario)