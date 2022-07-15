from django.contrib import admin
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list = ('taskName', 'description', 'status')


admin.site.register(Task, TaskAdmin)