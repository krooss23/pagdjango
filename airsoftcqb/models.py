from django.db import models

# Create your models here.

class Estado(models.Model):
    idEstado = models.AutoField(primary_key=True)
    nombreEstado = models.CharField(max_length=50)

    def estadosJugador(self):
        return "{}".format(self.nombreEstado)

    def __str__(self):
        return self.estadosJugador()

    

class RolPlayer(models.Model):
    idRolPlayer = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=50)

    def RolPlayer(self):
        return "{}".format(self.rol)

    def __str__(self):
        return self.RolPlayer()

class Equipo(models.Model):
    idEquipo = models.AutoField(primary_key=True)
    nombreEquipo = models.CharField(max_length=50)

    def Equipo(self):
        return "{}".format(self.nombreEquipo)

    def __str__(self):
        return self.Equipo()


class Player(models.Model): 
    idPlayer = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    edad = models.CharField(max_length=10)
    apellidos = models.CharField(max_length=15)
    rut = models.CharField(max_length=15)
    nombreTeam = models.CharField(max_length=50, verbose_name = 'Nombre Team')
    nick = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    idRolPlayer = models.ForeignKey(RolPlayer, null = True, blank = True, verbose_name = 'rolPlayer', on_delete = models.CASCADE)
    idEquipo = models.ForeignKey(Equipo, null = True, blank = True, verbose_name = 'equipo', on_delete = models.CASCADE)
    idEstado = models.ForeignKey(Estado, null = True, blank = True, verbose_name = 'estado', on_delete = models.CASCADE)



class Partida(models.Model):
    idPartida = models.AutoField(primary_key=True)
    lugar = models.CharField(max_length=50)
    fecha = models.DateField(null=True)
   


class Asignacion(models.Model):
    idAsignacion = models.AutoField(primary_key=True)
    idPlayer = models.ForeignKey(Player, null = True, blank = True, verbose_name = 'player', on_delete = models.CASCADE)
    idPartida = models.ForeignKey(Partida, null = True, blank = True, verbose_name = 'partida', on_delete = models.CASCADE)



















     













# estadoCivilId = models.ForeignKey(EstadoCivil, null = True, blank = True, verbose_name = 'Estado Civil', on_delete = models.CASCADE)