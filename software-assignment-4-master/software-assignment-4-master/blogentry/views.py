
from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import *
from .forms import BlogForm
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
def show_all(request):
    if request.method == "POST":
        form = BlogForm(request.POST)

        if form.is_valid():
            entry = form.save(commit=False)
            entry.owner = request.user
            entry.save()
            form.save_m2m()

    elif request.method == "GET":
        form = BlogForm()

    return render(request, "entry.html", {"entries": Entry.objects.filter(owner=request.user.id),
                                         "tags": Tag.objects.all()})

def get_one_entry(request, item_id):
    try:
        entry = Entry.objects.get(id=item_id, owner=request.user.id)
        return render(request, "blogentry.html", {"entry": entry})
    except Entry.DoesNotExist:
        raise Http404("We don't have any.")

