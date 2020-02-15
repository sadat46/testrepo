from django.shortcuts import render

# Create your views here.
def blog(request,*args,**kwargs):
   return render(request, "blog.html", {})
