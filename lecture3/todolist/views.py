from django.shortcuts import render

tasks = ["task_1", "task_2", "task_3"]

def index(request):
    cont = {"html_tasks": tasks}
    return render(request, "todolist/index.html", cont)
