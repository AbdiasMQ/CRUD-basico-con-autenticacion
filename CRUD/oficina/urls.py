from django.urls import path, include
from . import views
app_name = 'oficina'

urlpatterns = [
    path('', views.index, name='index'),
]
