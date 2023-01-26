from django.shortcuts import render
""" from .form import SignUpForm,UserCreationForm """
# Create your views here.


def login(request):
    return render(request,'login.html')


""" def signup(request):
    
    form = SignUpForm(request.POST)
    
    if form.is_valid:
        pass
    
    else:
        form = SignUpForm()
        
    context = {
        "form" : form
    }
    
    
     """
    