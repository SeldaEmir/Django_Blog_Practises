
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import *
from .forms import BlogForm

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
@permission_required('is_superuser')
def show_all_superuser(request):
    return render(request, "entry.html", {"entries": Entry.objects.all()})

def get_one_entry(request, item_id):
    try:
        entry = Entry.objects.get(id=item_id, owner=request.user.id)
        return render(request, "blogentry.html", {"entry": entry})
    except Entry.DoesNotExist:
        raise Http404("We don't have any.")


@permission_required('is_superuser')
def show_user_entries(request, userId):
    return render(request, "entry.html", {"entries": Entry.objects.filter(owner=userId)})
