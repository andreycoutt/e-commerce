from django.shortcuts import render
from django.http import HttpResponse

def helloWorld(request):
    return HttpResponse('Hello World')

def PagInicial(request):
    return render(request, 'inicio/home.html')