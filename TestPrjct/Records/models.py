# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=100)

def __str__(self):
    return self.Name
