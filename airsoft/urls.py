
from django.contrib import admin
from django.urls import path,include               




from airsoftcqb.views import rendertemplates, historia, replica, listado, createPlayer, cancha, vetado, deletePlayer,unban

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', rendertemplates, name="home"),
    path('historia/',historia,name='historia'),
    path('replica/',replica,name='replica'),
    path('cancha/',cancha,name='cancha'),
    path('listado/',listado,name='listado'),
    path('createPlayer/',createPlayer,name='createPlayer'),
    path('vetado/',vetado,name='vetado'),
    path('listado/deletePlayer/<int:id>', deletePlayer, name='deletePlayer'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('vetado/unban/<int:id>/<int:op>', unban, name='unban'),
    path('listado/unban/<int:id>/<int:op>', unban, name='unban'),






    
    
  
]
