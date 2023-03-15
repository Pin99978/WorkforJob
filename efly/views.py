from django.shortcuts import render ,  redirect
from django.http import HttpResponse ,JsonResponse
from .models import *


def efly(request):

    context = {}
    return render(request , 'efly/index.html',context)
