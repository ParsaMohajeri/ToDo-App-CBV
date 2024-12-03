# import part
from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView
from .models import Post
from django.views.generic import ListView,DetailView,FormView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
# ________________________________________________________________
# Create your views here.
class IndexView(TemplateView):
    """
    this is just normal view of the site
    """
    template_name="index.html"
    def get_context_data(self,**kwargs):
        context= super().get_context_data(**kwargs)
        context["name"]="parsa"
        context["posts"]=Post.objects.all()
        return context