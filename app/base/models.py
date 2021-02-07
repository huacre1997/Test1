from django.db import models
from django.contrib.auth.models import User

class ClaseModelo(models.Model):
    status=models.BooleanField(default=True)
    created=models.DateTimeField(verbose_name="Fecha de creación",auto_now_add=True)
    updated=models.DateTimeField(verbose_name="Fecha de modificación", auto_now=True)
    
    class Meta:
        abstract=True
        ordering = ['-created']