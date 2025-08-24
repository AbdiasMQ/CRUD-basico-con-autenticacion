from django.urls import path, include
#urls for auth views
from django.contrib.auth import views as auth_views
from . import views
from .views import SignUpView, LogoutMessageView, LoginView

app_name = "accounts"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),  
    path("logout/", LogoutMessageView.as_view(), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
]

