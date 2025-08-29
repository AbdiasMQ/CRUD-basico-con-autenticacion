from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.urls import reverse_lazy
from .models import oficina
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class oficinaListView(ListView):
    model = oficina
    template_name = 'oficina/oficina_lista.html'
    context_object_name = 'oficinas'

class oficinaDetailView(DetailView):
    model = oficina
    template_name = 'oficina/oficina_detalle.html'
    context_object_name = 'oficina'

class oficinaCreateView(LoginRequiredMixin, CreateView):
    model = oficina
    template_name = 'oficina/oficina_crear.html'
    fields = ['nombre', 'nombre_corto']
    success_url = reverse_lazy('oficina:oficina_lista')

class oficinaUpdateView(LoginRequiredMixin, UpdateView):
    model = oficina
    template_name = 'oficina/oficina_editar.html'
    fields = ['nombre', 'nombre_corto']
    success_url = reverse_lazy('oficina:oficina_lista')

class oficinaDeleteView(LoginRequiredMixin, DeleteView):
    model = oficina
    template_name = 'oficina/oficina_eliminar.html'
    success_url = reverse_lazy('oficina:oficina_lista')

class oficinaSearchView(ListView):
    model = oficina
    template_name = 'oficina/oficina_buscar.html'
    context_object_name = 'oficinas'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return oficina.objects.filter(Q(nombre__icontains=query) | Q(nombre_corto__icontains=query))
        return oficina.objects.none()