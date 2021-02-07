from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class ClaseModelo(models.Model):
    status=models.BooleanField(default=True);
    created=models.DateTimeField(verbose_name="Fecha de creación",auto_now_add=True)
    updated=models.DateTimeField(verbose_name="Fecha de modificación", auto_now=True)
    createdU=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    updatedU=models.IntegerField(settings.AUTH_USER_MODEL,blank=True,null=True)
    class Meta:
        abstract=True