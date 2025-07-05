from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView
from .models import Task
from django.views.generic import ListView,DetailView,FormView,CreateView,UpdateView,DeleteView
from .forms import TaskForm
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
# ________________________________________________________________
# Create your views here.


# class IndexView(TemplateView):
#     """
#     this is just normal view of the site
#     """
#     template_name="index.html"


    
class TaskListView(LoginRequiredMixin,ListView):
    login_url = "/accounts/login/"
    queryset=Task.objects.filter(status=True)
    # model=Post
    paginate_by=4
    ordering='-published_date'
    
    context_object_name="tasks"
    # def get_queryset(self):
    #     posts=Post.objects.filter(status=True)
        # return posts



class TaskDetailView(LoginRequiredMixin,DetailView):
    model=Task




class TaskCreateView(LoginRequiredMixin,CreateView):
    model=Task
    # fields=['author', 'title', 'content','status','category','published_date']
    form_class=TaskForm
    success_url='/'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class TaskEditView(LoginRequiredMixin,UpdateView):
    model=Task
    form_class=TaskForm
    success_url='/'

class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model=Task
    success_url="/"


