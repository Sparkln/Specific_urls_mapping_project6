from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first(request):
    return HttpResponse('<h1>I am beging of light</h1>')
def second(request):
    return HttpResponse('<h1>Abani getting job within 7 days</h1>')
