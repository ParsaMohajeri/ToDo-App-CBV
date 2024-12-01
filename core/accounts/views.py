# import part
from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView
from .models import Post
from django.views.generic import ListView,DetailView,FormView,CreateView,UpdateView,DeleteView
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

# _____________________________________________________________________
# Create your views here.
