from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Mesa, Comanda
from .forms import MesaForm, ComandaForm

class MesaListView(ListView):
    model = Mesa
    template_name = 'mesa/mesa_list.html'
    context_object_name = 'mesas'
    

class MesaCreateView(CreateView):
    model = Mesa
    form_class = MesaForm
    template_name = 'mesa/mesa_form.html'
    success_url = reverse_lazy('mesa:mesa_list')

class MesaUpdateView(UpdateView):
    model = Mesa
    form_class = MesaForm
    template_name = 'mesa/mesa_form.html'
    success_url = reverse_lazy('mesa:mesa_list')

class MesaDeleteView(DeleteView):
    model = Mesa
    template_name = 'mesa/mesa_delete.html'
    success_url = reverse_lazy('mesa:mesa_list')

class MesaDetailView(DetailView):
    model = Mesa
    template_name = 'mesa/mesa_detail.html'
    context_object_name = 'mesa'

class ComandaListView(ListView):
    model = Comanda
    template_name = 'mesa/comanda_list.html'
    context_object_name = 'comandas'


class ComandaCreateView(CreateView):
    model = Comanda
    form_class = ComandaForm
    template_name = 'mesa/comanda_form.html'
    success_url = reverse_lazy('mesa:comanda_list')

class ComandaUpdateView(UpdateView):
    model = Comanda
    form_class = ComandaForm
    template_name = 'mesa/comanda_form.html'
    success_url = reverse_lazy('mesa:comanda_list')


class ComandaDeleteView(DeleteView):
    model = Comanda
    template_name = 'mesa/comanda_delete.html'
    success_url = reverse_lazy('mesa:comanda_list')


class ComandaDetailView(DetailView):
    model = Comanda
    template_name = 'mesa/comanda_detail.html'
    context_object_name = 'comanda'

