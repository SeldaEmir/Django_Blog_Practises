__author__ = 'seldaemir'

from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^entries/(?P<item_id>[0-9]+)', get_one_entry),
    url(r'^entries/$', show_all),
    url(r'^entries/all/user/(?P<userId>[0-9]+)$', show_user_entries),
    url(r'^entries/all/$', show_all_superuser),
    url(r'^admin/', admin.site.urls),
    ]
