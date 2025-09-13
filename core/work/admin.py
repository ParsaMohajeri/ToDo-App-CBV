from django.contrib import admin
from .models import Task


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    model=Task
    list_display = ["is_done", "title", "created_date", "deadline"]
    ordering = ("created_date",)
    list_filter = ("title", "is_done")


admin.site.register(Task,TaskAdmin)
