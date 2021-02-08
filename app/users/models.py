from django.db import models
from business.models import Business

from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.conf import settings
from django.forms import model_to_dict

class CustomUser(AbstractUser):
    date=models.DateField(max_length=12,blank=True,null=True)
    tel=models.CharField(max_length=9,blank=True,null=True)
    dni=models.CharField(max_length=8,blank=True,null=True)
    image=models.ImageField(upload_to="users/%Y/%m/%d",null=True,blank=True)
    business=models.ManyToManyField(Business, verbose_name="Empresas",related_name="business_fk",blank=True)
    def __str__(self):
        return self.first_name+" "+self.last_name
    def get_image(self):
        if self.image:
            return '{}{}'.format(settings.MEDIA_URL,self.image)
        return '{}{}'.format(settings.STATIC_URL,"img/user.png")
    def toJSON(self):
        item=model_to_dict(self,exclude=["password","groups","user_permissions","business"])
        if self.last_login:
            item["last_login"]=self.last_login.strftime("%Y-%m-%d")
        item["date_joined"]=self.date_joined.strftime("%Y-%m-%d")
        item["image"]=self.get_image()
      

        return item