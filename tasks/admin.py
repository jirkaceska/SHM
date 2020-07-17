from django.contrib import admin

from .models import SignableTask, Task, Application

# Register your models here.
admin.site.register(SignableTask)
admin.site.register(Task)
admin.site.register(Application)
