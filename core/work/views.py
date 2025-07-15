# work/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.http import HttpResponseForbidden
from .models import Task
from .forms import TaskForm

class TaskListView(LoginRequiredMixin, ListView):
    login_url = "/accounts/login/"
    paginate_by = 4
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user).order_by('-deadline', 'created_date')

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = "task"

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('work:task-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TaskEditView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('work:task-list')

    def get_queryset(self):

        return Task.objects.filter(author=self.request.user, deadline__gt=timezone.now()) | Task.objects.filter(author=self.request.user, deadline__isnull=True)

    def get(self, request, *args, **kwargs):
        task = self.get_object()
        if task.deadline and task.deadline <= timezone.now():
            return HttpResponseForbidden("This task's deadline has passed and cannot be edited.")
        return super().get(request, *args, **kwargs)

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('work:task-list')

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)

def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk, author=request.user)
    task.is_done = not task.is_done
    task.save()
    return redirect('work:task-list')