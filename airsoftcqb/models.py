from django.db import models

# Create your models here.

class Estado(models.Model):
    idEstado = models.AutoField(primary_key=True)
    nombreEstado = models.CharField(max_length=50)

    def estadosJugador(self):
        return "{}".format(self.nombreEstado)

    def __str__(self):
        return self.estadosJugador()

class Player(models.Model): 
    idPlayer = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    edad = models.CharField(max_length=10)
    apellidos = models.CharField(max_length=15)
    rut = models.CharField(max_length=15)
    nombreTeam = models.CharField(max_length=50, verbose_name = 'Nombre Team')
    nick = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    idEstado = models.ForeignKey(Estado, null = True, blank = True, verbose_name = 'estado', on_delete = models.CASCADE)

    
    
    

class Team(models.Model):
    idTeam = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)



class Partida(models.Model):
    idPartida = models.AutoField(primary_key=True)
    dia = models.CharField(max_length=50)
    equipoA = models.CharField(max_length=50)
    equipoB = models.CharField(max_length=50)


class Moderador(models.Model):
     idModerador = models.AutoField(primary_key=True)
     nombre = models.CharField(max_length=50)
     apellido = models.CharField(max_length=50)
     replica = models.CharField(max_length=50)


class Cancha(models.Model):
    idCancha = models.AutoField(primary_key=True)
    evento = models.CharField(max_length=50)
    horario = models.CharField(max_length=50)
    dia = models.CharField(max_length=50)
    moderador = models.ForeignKey(Moderador, null = True, blank = True, verbose_name = 'moderador', on_delete = models.CASCADE)
    partida = models.ForeignKey(Partida, null = True, blank = True, verbose_name = 'partida', on_delete = models.CASCADE)


class EstadoPlayer(models.Model):
    idEstadoPlayer = models.AutoField(primary_key=True)
    player = models.ForeignKey(Player, null = True, blank = True, verbose_name = 'player', on_delete = models.CASCADE)
    cancha = models.ForeignKey(Cancha, null = True, blank = True, verbose_name = 'cancha', on_delete = models.CASCADE)
    estado = models.ForeignKey(Estado, null = True, blank = True, verbose_name = 'estado', on_delete = models.CASCADE)
    team   = models.ForeignKey(Team, null = True, blank = True, verbose_name = 'estado', on_delete = models.CASCADE)










     













# estadoCivilId = models.ForeignKey(EstadoCivil, null = True, blank = True, verbose_name = 'Estado Civil', on_delete = models.CASCADE)