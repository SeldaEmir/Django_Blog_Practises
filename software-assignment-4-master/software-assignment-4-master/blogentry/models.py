
from __future__ import unicode_literals
from django.db import models
from tags.models import Tag
from django.contrib.auth.models import User


class Entry(models.Model):

    name = models.CharField(max_length=220)
    description = models.CharField(max_length=520)
    owner = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag)

