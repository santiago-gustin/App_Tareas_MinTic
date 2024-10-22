from django.contrib import admin
from reglas.models import Regla
# Register your models here.


# Register your models here.
#ENVIAS AL PANE DE ADMINISTRACION EL MODEL

@admin.register(Regla)

class ReglaAdmin(admin.ModelAdmin):
    list_display = ['descripcion', 'id_user']

    