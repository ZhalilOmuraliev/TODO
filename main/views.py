from django.shortcuts import render, HttpResponse
from .models import TODO

def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = TODO.objects.all()
    return render(request, "test.html")

def second(request):
    return HttpResponse("test 2 page")

def third(request):
    return HttpResponse("This page is test3")

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = TODO(text=text)
    todo.save()
    return HttpResponse("Форма получена")

def delete_todo(request, id):
    todo = TODO.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo  TODO.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)