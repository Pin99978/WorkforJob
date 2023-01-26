from django.db import models

# Create your models here.

class Tool(models.Model):
    id_primary = models.IntegerField(primary_key=True)
    tools = models.CharField(max_length=20)
    fabs = models.CharField(max_length=20)
    
    
class CurAlarm(models.Model):
    id_primary = models.IntegerField(primary_key=True)
    tools = models.CharField(max_length=20)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True)
    

    