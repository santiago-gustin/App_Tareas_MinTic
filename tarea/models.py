from django.db import models
from reglas.models import Regla
from django.utils.html import format_html

# Create your models here.
class Tarea(models.Model):
    id_tarea = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    prioridad = models.CharField(max_length=20, blank=True, null=True)
    frecuencia = models.CharField(max_length=20, blank=True, null=True)
    id_regla = models.ForeignKey(Regla, on_delete=models.SET_NULL, null=True, db_column='id_regla')
    imagen = models.ImageField(upload_to='tareas/', null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'tarea'
        
    def __str__(self):
        return self.nombre if self.nombre else 'Tarea sin nombre'

    def mostrar_imagen(self):
        if self.imagen: 
            return format_html('<img src="{}" width="50" height="50">'.format(self.imagen.url))
        else:
            return ''
        
    mostrar_imagen.short_description = 'Imagen'