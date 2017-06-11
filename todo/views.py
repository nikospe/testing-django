import json
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

# def post

# def delete