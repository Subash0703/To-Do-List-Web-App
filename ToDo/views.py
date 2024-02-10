from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import TodoList
from .models import MyTodoList



# Create your views here.


def todolist(request):
    todo = MyTodoList.objects.all()
    return render(request,"Todolist\\todolisttable.html", context={"todo":todo})

def addnewtask(request):
    if request.method == "POST":
        if (request.POST.get("task") and request.POST.get("time_interval")):
            todoadd = MyTodoList()
            todoadd.task = request.POST.get("task")
            todoadd.time_interval = request.POST.get("time_interval")
            todoadd.save()
            return redirect("/task/todo/")
        else:
            return HttpResponse("<h3>Some Inputs Are Missing Try to Fill Essentials.........</h3>")

    form = TodoList()
    return render(request,"Todolist\\addtask.html", context={"form": form})

def deltask(request, id):
    task = MyTodoList.objects.get(id=id)
    task.delete()
    return redirect("/task/todo/")
