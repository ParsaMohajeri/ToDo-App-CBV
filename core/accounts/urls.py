from django.urls import path
from .views import CustomLoginView , RegisterPage , CustomLogoutView
from . import views
from django.contrib.auth.views import LogoutView

app_name = "accounts"

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path("register/", RegisterPage.as_view(), name="register"),
]
