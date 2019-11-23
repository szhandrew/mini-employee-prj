from django.db import models

# Create your models here. 
 
class UserInfor(models.Model):
 
    nm=models.CharField(max_length=64)
    em=models.CharField(max_length=64)
    pos=models.CharField(max_length=64)
    pn=models.CharField(max_length=64)
    sl=models.CharField(max_length=64)
    dh=models.CharField(max_length=64)
