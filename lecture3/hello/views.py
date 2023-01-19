from django.shortcuts import render
from django.http import HttpResponse

def index(request): # Request represents the user request variable
    return render(request, "hello/index.html")

def greet(request, in_name):
    out_str = "Hello " + in_name.capitalize()
    cont = {"html_name": in_name.capitalize()} # html_name is between double curly braces in the hello/greet.html template
    return render(request, "hello/greet.html", cont)
