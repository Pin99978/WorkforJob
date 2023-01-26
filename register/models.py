from django.db import models

# Create your models here.

class User(models.Model):
    id_User     = models.IntegerField(primary_key=True)
    account     = models.CharField(max_length=20      )
    password    = models.CharField(max_length=20      )
    fablocation = models.CharField(max_length=5       )


