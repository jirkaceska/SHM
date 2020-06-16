from django.contrib import admin
from .models import SignableTask, TaskState, Task

# Register your models here.
admin.site.register(SignableTask)
admin.site.register(Task)
admin.site.register(TaskState)
