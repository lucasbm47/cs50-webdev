from django.shortcuts import render
from django.http import HttpResponse
import random

def index(request): # Request represents the user request variable
    return render(request, "hello/index.html")

def greet(request, in_name):
    out_str = "Hello " + in_name.capitalize()
    lucky_number = str(random.random()*10)

    cont = {"html_name": in_name.capitalize(),
            "html_lucky_number": lucky_number}

    # html_name is between double curly braces in the hello/greet.html template and allows to render the value of a variable in the HTML
    # The keys of the cont dictionary must match the names in the HTML template between curly braces
    return render(request, "hello/greet.html", cont)
