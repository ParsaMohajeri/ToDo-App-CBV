from django import forms
from .models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ["title", "content", "deadline"]
        widgets = {
            "deadline": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }
        labels = {
            "title": "Task Title",
            "content": "Description",
            "deadline": "Deadline (Optional)",
        }
