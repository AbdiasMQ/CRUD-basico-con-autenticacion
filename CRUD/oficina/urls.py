from django.urls import path, include
from . import views

app_name = 'oficina'

urlpatterns = [
    path('lista/', views.OficinaListView.as_view(), name='oficina_lista'),
    path('buscar/', views.OficinaSearchView.as_view(), name='oficina_buscar'),
    path('crear/', views.OficinaCreateView.as_view(), name='oficina_crear'),
    path('editar/<int:pk>/', views.OficinaUpdateView.as_view(), name='oficina_editar'),
    path('eliminar/<int:pk>/', views.OficinaDeleteView.as_view(), name='oficina_eliminar'),
    path('detalle/<int:pk>/', views.OficinaDetailView.as_view(), name='oficina_detalle'),
]