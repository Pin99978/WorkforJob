from django.contrib import admin

# Register your models here.


from .models import *


admin.site.register(Tool)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

