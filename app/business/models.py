from django.db import models
  
from django.forms import model_to_dict

from django.dispatch import receiver
from base.models import ClaseModelo
from django.conf import settings
from django.forms import model_to_dict

class Business(ClaseModelo):
    name=models.CharField( max_length=100,unique=True)
    ruc=models.CharField( max_length=11,null=True,blank=True)
    # users = models.ManyToManyField(settings.AUTH_USER_MODEL,verbose_name="Usuarios", blank=True)
    def __str__(self):
        return self.name
    def toJSON(self):
        item = model_to_dict(self)
        item["created"]=self.created.strftime("%Y-%m-%d %H:%M:%S")
        item["updated"]=self.updated.strftime("%Y-%m-%d %H:%M:%S")

        return item
    