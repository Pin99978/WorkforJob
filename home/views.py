from django.shortcuts import render , get_object_or_404


# Import the  database here
from .models import Tool

# Create your views here.

# base home html
def home(request):
    return  render(request , 'index.html')

# Add the data to home.html

def tool_info(request, pk):
    tool = get_object_or_404(Tool, pk=pk)
    tool_info = {'info': tool}
    return render(request, 'index.html', tool_info)


def tool_list(request):
    
    tool = Tool.objects.all()
    tool_list = {'toollist' : tool}
    return render(request, 'index.html', tool_list)

