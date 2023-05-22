
from django.contrib import admin
from django.urls import path


from airsoftcqb.views import rendertemplates, historia, replica

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', rendertemplates, name="home"),
    path('historia/',historia,name='historia'),
    path('replica/',replica,name='replica'),
    path('replica/',replica,name='cancha'),
  
]
