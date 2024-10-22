from django.db import models
from tarea.models import Tarea
from users.models import User

# Create your models here.

class Realiza(models.Model):
    id_realiza = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, db_column='id_user')
    id_tarea = models.ForeignKey(Tarea, on_delete=models.SET_NULL, null=True, db_column='id_tarea')
    estado = models.CharField(max_length=50, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'realiza'




