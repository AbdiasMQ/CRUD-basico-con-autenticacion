from django.urls import path, include
from . import views

app_name = 'oficina'

urlpatterns = [
    path('lista/', views.oficinaListView.as_view(), name='oficina_lista'),
    path('buscar/', views.oficinaSearchView.as_view(), name='oficina_buscar'),
    path('crear/', views.oficinaCreateView.as_view(), name='oficina_crear'),
    path('editar/<int:pk>/', views.oficinaUpdateView.as_view(), name='oficina_editar'),
    path('eliminar/<int:pk>/', views.oficinaDeleteView.as_view(), name='oficina_eliminar'),
    path('detalle/<int:pk>/', views.oficinaDetailView.as_view(), name='oficina_detalle'),
]