from django.db import models
from django.db.models.base import Model
from django.utils.translation import deactivate

# Create your models here.
class Serie(models.Model):
    nombre= models.CharField(max_length=100)
    categoria=models.CharField(max_length=20)
    rating=models.IntegerField(default=0)
    
    def __str__(self):
        return self.nombre
    