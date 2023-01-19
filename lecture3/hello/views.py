from django.shortcuts import render
from django.http import HttpResponse

def index(request): # Request represents the user request variable
    return HttpResponse("Hello world!")

def greet(request, in_name):
    out_str = "Hello " + in_name.capitalize()
    return HttpResponse(out_str)
