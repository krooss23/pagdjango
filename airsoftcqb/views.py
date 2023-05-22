from django.shortcuts import render

# Create your views here.

def rendertemplates(request):
    return render(request, 'templatesairsoftcqb/inicio.html')


def historia(request):
    return render(request, 'templatesairsoftcqb/historia.html' )


def replica(request):
    return render(request, 'templatesairsoftcqb/replica.html' )

def cancha(request):
    return render(request, 'templatesairsoftcqb/cancha.html' )