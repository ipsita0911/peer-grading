from django.contrib import admin
from django.urls import path
from django.urls import include, path
from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^$', index),
    url(r'^(?P<rollNumber>\w+)/student/$', student_home),
    url(r'^(?P<question_number>\w+)/(?P<rollNumber>\w+)/submit/$', submit_program),
    url(r'^(?P<question_number>\w+)/(?P<rollNumber>\w+)/student/$', to_grade),
    url(r'^(?P<rollNumber>\w+)/task_student/$', task),
    url(r'^(?P<question_number>\w+)/(?P<uniqueID>\w+)/(?P<rollNumber>\w+)/grade/$', grade),

]
