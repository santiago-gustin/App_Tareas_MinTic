from django.contrib import admin
from realiza.models import Realiza
# Register your models here.
# Cambiar el título de la página de administración
admin.site.site_header = "Administración de Mi Proyecto"  # Encabezado superior
admin.site.site_title = "Mi Proyecto Admin"  # Título en la pestaña del navegador
admin.site.index_title = "Bienvenido al Panel de Administración"  # Título del índice



# Register your models here.
#ENVIAS AL PANE DE ADMINISTRACION EL MODEL

@admin.register(Realiza)

class RealizaAdmin(admin.ModelAdmin):
    list_display = ['id_user', 'id_tarea', 'estado', 'fecha']