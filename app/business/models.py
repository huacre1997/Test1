from django.db import models
  
from django.forms import model_to_dict

from django.dispatch import receiver
from base.models import ClaseModelo

class Business(ClaseModelo):
    name=models.CharField( max_length=100,unique=True)
    ruc=models.CharField( max_length=11,null=True,blank=True)
   