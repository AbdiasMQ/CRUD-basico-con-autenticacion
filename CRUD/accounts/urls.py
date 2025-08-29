from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),   # <- aquí
    path('logout/', views.LogoutMessageView.as_view(), name='logout'),  # <- si quieres tu template de logout
    path('signup/', views.SignUpView.as_view(), name='signup'),
]

