from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

class Tool(models.Model):
    
    # id=
    name  =models.CharField(max_length=10)
    # null = Ture -> meaning  it can  be empty
    # blank = Ture -> meaning  whenever pass save reponse , it can be 
    series=models.CharField(max_length=10)
    type  =models.CharField(max_length=10)
    fab   =models.CharField(max_length=10)
    ip    =models.CharField(max_length=20)  
    
    
    def __str__(self):
        return self.name
class Module(models.Model):
    
    pass    
    
    
class CurrentAlarm(models.Model):
    tool  = models.ForeignKey(Tool, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class ToolAlarm(models.Model):
    
    # CASCADE : jf tool is deleted , all the alarm msg are removed
    tool  = models.ForeignKey(Tool, on_delete=models.CASCADE)
    
    alarmtype = models.CharField(max_length=10)
    alarmmsg =  models.CharField(max_length=50)
    def __str__(self):
        return self.name     
    
