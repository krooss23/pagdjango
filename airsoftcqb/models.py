from django.db import models

# Create your models here.

nombre = models.CharField(max_length=50)
edad = models.CharField(max_length=10)
color = models.CharField(max_length=15)
nombreTeam = models.CharField(max_length=50)