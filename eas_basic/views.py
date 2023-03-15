from django.shortcuts import render , redirect
from django.http import HttpResponse ,JsonResponse

from django.utils import timezone
from .models import *


# this is for a retricted Page
from django.contrib.auth.decorators import login_required


   
    # {'id': 1 , 'name': 'AKT5-10'},
    # {'id': 2 , 'name': 'AKT6-4'}




def home(request):
    tools = Tool.objects.all()
    current_time = get_current_time(request)
    context = {'tool' : tools , 'current_time' : current_time}
    return render(request , 'eas_basic/home.html',context)


def login(request):
    return HttpResponse("hello user")




def get_current_time(request):
    current_time = timezone.now().strftime('%Y-%m-%D %H:%M:%S')
    print(current_time)
    return HttpResponse(current_time)