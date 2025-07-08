
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.shortcuts import redirect

from .forms import CustomAuthenticationForm


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('accounts:login')


class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    authentication_form = CustomAuthenticationForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("work:task-list")


class RegisterPage(FormView):
    template_name = "registration/register.html"
    form_class = CustomAuthenticationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("work:task-list")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("work:task-list")
        return super().get(*args, **kwargs)