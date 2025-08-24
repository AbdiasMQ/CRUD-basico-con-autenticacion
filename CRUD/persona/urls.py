from django.urls import path, include
from . import views
from django.urls import path
app_name = 'persona'

urlpatterns = [
    path('lista/', views.PersonaListView.as_view(), name='persona_lista'),
    path('buscar/', views.PersonaSearchView.as_view(), name='persona_buscar'),
    path('crear/', views.PersonaCreateView.as_view(), name='persona_crear'),
    path('editar/<int:pk>/', views.PersonaUpdateView.as_view(), name='persona_editar'),
    path('eliminar/<int:pk>/', views.PersonaDeleteView.as_view(), name='persona_eliminar'),
    path('detalle/<int:pk>/', views.PersonaDetailView.as_view(), name='persona_detalle'),
]
