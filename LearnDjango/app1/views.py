from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import os

APPNAME='app1'

# Reasoning for the project
def page1(request):
    return render(request, 'index.html')

# Talks about the models
def page3(request):
    return render(request, 'index.html')


