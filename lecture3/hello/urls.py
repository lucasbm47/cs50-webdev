from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"), # When the user visits the empty url, I want to execute the views.index function
    path("<str:in_name>", views.greet, name = "greet")
    # "<str:in_name>" means that the route can be any string, and we are giving it the name of "name" to the parameter
]