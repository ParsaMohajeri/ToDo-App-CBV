from django.contrib import admin
from .models import Task
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display=['author','title','created_date','deadline']




admin.site.register(Task)