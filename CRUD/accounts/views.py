from django.shortcuts import render

# Create your views here.
#cv for signup view
from django.views.generic import CreateView, TemplateView

from django.urls import reverse_lazy #es importante
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("accounts:login")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Sign Up'
        return context

class LogoutMessageView(TemplateView):
    template_name = 'accounts/logout_message.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'desloguearse'
        return context

class LoginView(auth_views.LoginView):
    template_name = 'registration/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesión'
        return context
