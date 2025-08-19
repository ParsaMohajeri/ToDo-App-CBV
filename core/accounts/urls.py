from django.urls import path,include
from .views import CustomLoginView , RegisterPage , CustomLogoutView
from . import views
from django.contrib.auth.views import LogoutView

app_name = "accounts"

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path("register/", RegisterPage.as_view(), name="register"),
    path("", include("django.contrib.auth.urls")),
    # path('api/v1/', include('accounts.api.v1.urls')),
    path("api/v1/", include("djoser.urls")),
    path("api/v1/", include("djoser.urls.jwt")),
]
