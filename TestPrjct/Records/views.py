# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from Records.forms import PersonForm
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Person(request):
    form_class = PersonForm

    return render(request, 'Person.html', {
        'form': form_class,
    })

def index(request):
    return HttpResponse("Hi there you are at the Records page")
