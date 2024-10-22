from django.contrib import admin
from familias.models import Familia

# Register your models here.
#ENVIAS AL PANE DE ADMINISTRACION EL MODEL

@admin.register(Familia)

class FamiliaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'cantidad_integrantes']