from django.http import *
from django.shortcuts import render
from blogentry.models import *

# Create your views here.

def signup(request):

    if request.method == "POST":
        User.objects.create_user(username=request.POST.get("username"),
                            password=request.POST.get("password"))
        return HttpResponse("Success!")
    return render(request, "register.html")

def login(request):
    if request.method == "POST":
        username = "Welcome " + request.user.username + "!"
        return render(request, "entry.html", {"entries": Entry.objects.filter(owner=request.user.id),
                                              "username": username,
                                              "tags": Tag.objects.all()})
    return render(request, "login.html")

