from django.urls import path 
from . import views


urlpatterns = [
    path('efly/' , views.efly, name = "efly"),    

]
