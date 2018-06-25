from django.contrib import admin

from personal.models import ToDo

from .to_do import ToDoAdmin

admin.site.register(ToDo, ToDoAdmin)
