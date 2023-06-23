from django.contrib import admin
from .models import Player, Estado


# Register your models here.



@admin.register(Player)
class Player (admin.ModelAdmin):
    lista = ('nombre','edad','apellidos','rut','nombreTeam','nick','correo')

@admin.register(Estado)
class Estado(admin.ModelAdmin):
    list_display = ('idEstado', 'nombreEstado')

  



