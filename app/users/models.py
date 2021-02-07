from django.db import models

  
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    date=models.CharField(max_length=8)
    cel=models.CharField(max_length=8)
    dni=models.CharField(max_length=8)

    image=models.ImageField(upload_to="users/%Y/%m/%d",null=True,blank=True)
    
# class Roles(models.Model):
#     name= models.CharField(max_length="100")