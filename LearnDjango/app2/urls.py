from django.urls import include, path
from django.conf.urls import url

import sys
import mainapp
from . import views

app_name = 'app2'

urlpatterns = [
    path(r''            , mainapp.views.index ,            name='index'),
    path(r'getmenu/'    , views.getmenu,                    name='menu'),
    path(r'runexp/'     , views.runexp,           name='Run experiment'),
    path(r'runexp_1/'   , views.runexp_1,         name='Run experiment 1'),
    path(r'runexp_2/'   , views.runexp_2,         name='Run experiment 2'),
    path(r'runexp_3/'   , views.runexp_3,         name='Run experiment 3'),
]
