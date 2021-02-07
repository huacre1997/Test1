from django.db import models
from business.models import Business
  
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    date=models.CharField(max_length=8,blank=True)
    cel=models.CharField(max_length=8,blank=True)
    dni=models.CharField(max_length=8,blank=True)

    image=models.ImageField(upload_to="users/%Y/%m/%d",null=True,blank=True)
    business=models.ManyToManyField(Business, verbose_name="Empresas",related_name="business_fk",blank=True)
   
# class Roles(models.Model):
#     name= models.CharField(max_length="100")