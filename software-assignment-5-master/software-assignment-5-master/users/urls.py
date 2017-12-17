from django.conf.urls import url, include

from .views import *
from blogentry import views

urlpatterns = [
    url(r'^register/$', signup),
    url(r'', include("django.contrib.auth.urls")),
    url(r'^login/blog/entries/$', views.show_all),

]
