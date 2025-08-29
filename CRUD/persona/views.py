from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy    
from .models import Persona 
from django.contrib.auth.mixins import LoginRequiredMixin

#vista de lista de persona
class PersonaListView(ListView):
    model = Persona
    template_name = "persona/persona_lista.html"
    context_object_name = "persona"
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Persona.objects.filter(Q(name__icontains=query) | Q(apellido__icontains=query))
        return Persona.objects.all()
    
    def paginate_queryset(self, queryset, page_size):
        return super().paginate_queryset(queryset, page_size)

#persona detalle
class PersonaDetailView(DetailView):
    model = Persona
    template_name = "persona/persona_detalle.html"
    context_object_name = "persona"
    

#persona editar
class PersonaUpdateView(LoginRequiredMixin, UpdateView):
    model = Persona
    template_name = "persona/persona_editar.html"
    context_object_name = "persona"
    fields = ["nombre", "apellido", "edad", "oficina"]
    success_url = reverse_lazy("persona:persona_lista")

#persona eliminar
class PersonaDeleteView(LoginRequiredMixin, DeleteView):
    model = Persona
    template_name = "persona/persona_eliminar.html"
    context_object_name = "persona"
    success_url = reverse_lazy("persona:persona_lista")

#persona buscar
class PersonaSearchView(LoginRequiredMixin, ListView):
    model = Persona
    template_name = "persona/persona_buscar.html"
    context_object_name = 'persona'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Persona.objects.filter(
                Q(nombre__icontains=query) |
                Q(apellido__icontains=query) |
                Q(edad__icontains=query) 
            )
        return Persona.objects.none()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Buscar Persona'
        return context

#persona crear
class PersonaCreateView(LoginRequiredMixin, CreateView):
    model = Persona
    template_name = "persona/persona_crear.html"
    context_object_name = "persona"
    fields = ["nombre", "apellido", "edad", "oficina"]
    success_url = reverse_lazy("persona:persona_lista")
