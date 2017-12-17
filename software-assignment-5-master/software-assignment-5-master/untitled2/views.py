__author__ = 'seldaemir'

from django.http import HttpResponse, Http404
from django.shortcuts import render
'''
my_todos = ["go shopping", "get eggs", "bake cake", "watch tv"]

def show_todo (request):

   return render(request, "my_todos.html", {"todos": my_todos})

def get_todo(request, todo_id):
    try:
        return HttpResponse(my_todos[int(todo_id)])
    except IndexError:
        raise Http404("We dont have any todo.")
'''