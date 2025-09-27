from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.urls import reverse_lazy
from .models import Oficina
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
# Create your views here.

class OficinaListView(ListView):
    model = Oficina
    template_name = 'oficina/oficina_lista.html'
    context_object_name = 'oficinas'
    paginate_by = 10

class OficinaDetailView(LoginRequiredMixin, DetailView):
    model = Oficina
    template_name = 'oficina/oficina_detalle.html'
    context_object_name = 'oficina'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['persona'] = self.object.persona.all()
        return context

class OficinaCreateView(LoginRequiredMixin, CreateView):
    model = Oficina
    template_name = 'oficina/oficina_crear.html'
    fields = ['nombre', 'nombre_corto']
    success_url = reverse_lazy('oficina:oficina_lista')

class OficinaUpdateView(LoginRequiredMixin, UpdateView):
    model = Oficina
    template_name = 'oficina/oficina_editar.html'
    fields = ['nombre', 'nombre_corto']
    success_url = reverse_lazy('oficina:oficina_lista')

class OficinaDeleteView(LoginRequiredMixin, DeleteView):
    model = Oficina
    template_name = 'oficina/oficina_eliminar.html'
    success_url = reverse_lazy('oficina:oficina_lista')

class OficinaSearchView(ListView):
    model = Oficina
    template_name = 'oficina/oficina_buscar.html'
    context_object_name = 'oficinas'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Oficina.objects.filter(Q(nombre__icontains=query) | Q(nombre_corto__icontains=query))
        return Oficina.objects.none()