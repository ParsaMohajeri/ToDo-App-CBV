from celery import shared_task
from celery.schedules import crontab
from django.utils import timezone
from time import sleep
from .models import Task
from datetime import timedelta
from django.utils.timezone import now, timedelta





@shared_task
def delete_old_done_tasks():
    task = (
        Task.objects
        .filter(created_date__lte=now()-timedelta(hours=24), is_done=True)
        .order_by("created_date") 
        .first()
    )
    
    if task:
        task.delete()
        return f"Deleted task {task.id}"
    return "No tasks to delete"