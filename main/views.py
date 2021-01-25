from django.shortcuts import render, HttpResponse
from .models import todo

def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html")

def second(request):
    return HttpResponse("test 2 page")

def third(request):
    return HttpResponse("This page is test3")

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return HttpResponse("Форма получена")

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo  ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)

def close_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test)