from django.contrib import admin

from .models import Question, Test


admin.site.register(Question)
admin.site.register(Test)