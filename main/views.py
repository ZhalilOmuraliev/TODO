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

