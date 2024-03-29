from django.shortcuts import render, redirect
from .models import Player, Estado
from .forms import FormPlayer, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.

def rendertemplates(request):
    return render(request, 'templatesairsoftcqb/inicio.html')


def historia(request):
    return render(request, 'templatesairsoftcqb/historia.html' )

def replica(request):
    return render(request, 'templatesairsoftcqb/replica.html' )

def cancha(request):
    return render(request, 'templatesairsoftcqb/cancha.html' )



def prueba(request):
    return render(request, 'templatesairsoftcqb/prueba.html' )






def listado(request):
    players = Player.objects.all()
    data = {'players': players}
    return render(request, 'templatesairsoftcqb/listado.html', data )

def createPlayer(request):
    frm = FormPlayer ()
    if(request.method=='POST'):
        frm = FormPlayer (request.POST)
        if(frm.is_valid()):
            frm.save()
            return redirect('createPlayer')
    data = {'frm': frm}
    return render(request, 'templatesairsoftcqb/createPlayer.html', data )

def vetado(request):
    vetadi = Player.objects.filter(idEstado = 2)
    data = {'vetadi': vetadi}
    return render(request, 'templatesairsoftcqb/vetado.html', data )

def deletePlayer(request, id):
    players = Player.objects.get(idPlayer = id)
    players.delete()
    return redirect('listado')


def unban(request, id,op):
    players = Player.objects.get(idPlayer = id)
    if(op == 2):     
        estado = Estado.objects.get(idEstado = 1)
        mensaje = "vetado"
    if(op == 1):     
        estado = Estado.objects.get(idEstado = 2)
        mensaje = "listado"
    players.idEstado = estado
    print(players.idEstado)
    players.save() 
    return redirect(mensaje)


def registro(request):
    data={
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")
        data['form'] = formulario



    return render(request, 'registration/registro.html', data)