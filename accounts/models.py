from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    USER_TYPE_CHOICES = (
      (1, 'patient'),
      (2, 'hospital'),
      (3, 'admin'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,default=1)
    
class Hospital_User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    sido = models.CharField(max_length=20,)
    gungu = models.CharField(max_length=20,blank = True)
    dong = models.CharField(max_length=20,blank = True)
    addr = models.CharField(max_length = 50,blank = True)
    tel = models.CharField(max_length=50,blank = True)

class Personal_User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True,blank = True)
    addr = models.CharField(max_length=100,blank = True)
    phone = models.CharField(max_length=50,blank = True)


#class Personel_User(model.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)

    #hospital_name = models.CharField(max_length=100)