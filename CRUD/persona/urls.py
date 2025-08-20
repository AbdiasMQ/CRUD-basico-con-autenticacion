from django.urls import path, include
from . import views

app_name = 'persona'
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
