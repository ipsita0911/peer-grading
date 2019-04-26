from django.contrib import admin
from .models import *

admin.site.register(Question)
# Register your models here.
admin.site.register(Student)
admin.site.register(Submission)
admin.site.register(Marks)
