from django.contrib import admin
from .models import Player, Estado, RolPlayer, Equipo


# Register your models here.



@admin.register(Player)
class Player (admin.ModelAdmin):
    lista = ('nombre','edad','apellidos','rut','nombreTeam','nick','correo')

@admin.register(Estado)
class Estado(admin.ModelAdmin):
    list_display = ('idEstado', 'nombreEstado')



@admin.register(RolPlayer)
class RolPlayer(admin.ModelAdmin):
    list_display = ('idRolPlayer', 'rol')

@admin.register(Equipo)
class Equipo(admin.ModelAdmin):
    list_display = ('idEquipo', 'nombreEquipo')



  



