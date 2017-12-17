__author__ = 'seldaemir'

from django.http import HttpResponse, Http404
from django.shortcuts import render
from models import entrylist
from .models import *
my_todos = ["go shopping", "get eggs", "bake cake", "watch tv"]

def show_todo (request):

   return render(request, "my_todos.html" , {"todos": my_todos})

def get_todo(request, todo_id):
    try:
        return HttpResponse(my_todos[int(todo_id)])
    except IndexError:
        raise Http404("We dont have any todo.")

def show_all_entries(request):
    return render(request, "forListAll.txt", {"list":entrylist})

def get_one_entry(request, entryid):
    try:
        return render(request, "forListOne.txt", {"entry_id":int(entryid)+1,
                                                  "selected_word":entrylist[int(entryid)][0],
                                                  "selected_meaning":entrylist[int(entryid)][1]})

    except IndexError:
        raise Http404("We dont have any entry")

