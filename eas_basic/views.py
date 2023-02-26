from django.shortcuts import render , redirect
from django.http import HttpResponse



tools = [
    
    {'id': 1 , 'name': 'AKT5-10'},
    {'id': 2 , 'name': 'AKT6-4'}

]


def home(request):
    context = {'tool': tools}
    return render(request , 'eas_basic/home.html',context)


def login(request):
    return HttpResponse("hello user")

def tool(request,pk):
    
    return HttpResponse(pk)