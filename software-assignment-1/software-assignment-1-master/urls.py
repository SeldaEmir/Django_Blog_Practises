"""assignment1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpResponse, Http404
from django.shortcuts import render


my_todos = ["go shopping", "get eggs", "bake cake", "watch tv"]


def show_todo (request):

   return render(request, "my_todos.html" , {"todos": my_todos})

def get_todo(request, todo_id):
    try:
        return HttpResponse(my_todos[int(todo_id)])
    except IndexError:
        raise Http404("we dont have any.")

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/entries', show_todo),
    url(r'^blog/entries/(?P<todo_id>[0-9]+)', get_todo)
]

