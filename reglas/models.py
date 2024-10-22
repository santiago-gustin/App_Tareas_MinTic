from django.db import models
from users.models import User

# Create your models here.
class Regla(models.Model):
    id_regla = models.AutoField(primary_key=True)
    descripcion = models.TextField(blank=True, null=True)
    id_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'regla'

    def __int__(self):
        return self.id_regla if self.id_regla else 'Sin nombre'