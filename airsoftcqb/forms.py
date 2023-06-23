from django import forms
from .models import Player



opciones = [('vetado', 'Vetado'), ('activo', 'Activo')]

class FormPlayer(forms.ModelForm):
   
    nombre = forms.CharField()
    edad = forms.CharField()
    apellidos = forms.CharField()
    rut = forms.CharField()
    nombreTeam = forms.CharField()
    nick = forms.CharField()
    correo = forms.CharField()
    # idEstado = forms.ChoiceField()

    nombre.widget.attrs['class']='form-control'
    edad.widget.attrs['class']='form-control'
    apellidos.widget.attrs['class']='form-control'
    rut.widget.attrs['class']='form-control'
    nombreTeam.widget.attrs['class']='form-control'
    nick.widget.attrs['class']='form-control'
    correo.widget.attrs['class']='form-control'
    # idEstado.widget.attrs['class']='form-control'
    



    class Meta:
        model = Player
        fields = '__all__'

     


           
   