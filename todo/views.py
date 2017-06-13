import json
import sys
from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

def get_all(request):
    todos = Todo.objects.all()
    json_array = []

    for todo in todos:
        json_array.append(todo.to_json())

    return HttpResponse(json.dumps(json_array), content_type='application/json')

# def get_single
def get_single(request, id):
    todo = Todo.objects.get(pk=id)

    return HttpResponse(json.dumps(todo.to_json()))

# def post
def post(request, text):
    todo = Todo(text=text)
    todo.save()

    todos = Todo.objects.all()
    json_array = []

    for todo in todos:
        json_array.append(todo.to_json())

    return HttpResponse(json.dumps(json_array), content_type='application/json')    

# def delete
def delete(request):
    Todo.objects.all().delete()
    todos = Todo.objects.all()

    json_array = []

    for todo in todos:
        json_array.append(todo.to_json())

    return HttpResponse(json.dumps(json_array), content_type='application/json')
