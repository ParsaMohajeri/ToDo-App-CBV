from django.contrib import admin
from .models import Task
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display=['author','title','status','created_date','published_date']




admin.site.register(Task)