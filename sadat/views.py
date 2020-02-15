from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseRedirect

def home(request,*args,**kwargs):
   return render(request, "index.html", {})

def projects(request):
    return render(request, "projects.html",{})

def tutorial(request):
    return render(request, "tutorial.html",{})
