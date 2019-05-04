from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.



def home_view(request,*args, **kwargs):
    print(args, kwargs)
    
    #return HttpResponse("<h1>Hellu")
    return render(request, "home.html", {})

def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Contact")