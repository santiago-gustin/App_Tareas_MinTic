from django.db import models


# Create your models here.
class Familia(models.Model):
    id_familia = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    cantidad_integrantes = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'familia'