from django.shortcuts import render
from django.http import HttpResponse

def greeting(request):
    s=render(request,'exam/temp2.html')
    return (s)
    # Create your views here.
def showContact(request):
   s="<h1>my website</h1>"
   s+="<h2>my name</h2>"
   s+="<p>mobile:8340270054</p>"
   s+="<p>email:ak788955@gmail.com</p>"
   return HttpResponse(s)
def about(request):
  s+="<h1>this is about page</h1>"
  return HttpResponse(s)
