from django.db import models

# Create your models here.


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
    
class User(models.Model):
    pass
    # id=
    # NTaccount


class Currentalamr(models.Model):
    pass