from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Fornecedor, EstoqueProdutos
from .forms import FornecedorForm, EstoqueProdutosForm

class FornecedorListView(ListView):
    model = Fornecedor
    template_name = 'estoque/fornecedor_list.html'
    context_object_name = 'fornecedores'

class FornecedorCreateView(CreateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'estoque/fornecedor_form.html'
    success_url = reverse_lazy('estoque:fornecedor_list')

class FornecedorUpdateView(UpdateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'estoque/fornecedor_form.html'
    success_url = reverse_lazy('estoque:fornecedor_list')

class FornecedorDeleteView(DeleteView):
    model = Fornecedor
    template_name = 'estoque/fornecedor_delete.html'
    success_url = reverse_lazy('estoque:fornecedor_list')

class FornecedorDetailView(DetailView):
    model = Fornecedor
    template_name = 'estoque/fornecedor_detail.html'
    context_object_name = 'fornecedor'

class EstoqueProdutosListView(ListView):
    model = EstoqueProdutos
    template_name = 'estoque/estoque_list.html'
    context_object_name = 'estoqueprodutos'

class EstoqueProdutosCreateView(CreateView):
    model = EstoqueProdutos
    form_class = EstoqueProdutosForm
    template_name = 'estoque/estoque_form.html'
    success_url = reverse_lazy('estoque:estoque_list')

class EstoqueProdutosUpdateView(UpdateView):
    model = EstoqueProdutos
    form_class = EstoqueProdutosForm
    template_name = 'estoque/estoque_form.html'
    success_url = reverse_lazy('estoque:estoque_list')

class EstoqueProdutosDeleteView(DeleteView):
    model = EstoqueProdutos
    template_name = 'estoque/estoque_delete.html'
    success_url = reverse_lazy('estoque:estoque_list')

class EstoqueProdutosDetailView(DetailView):
    model = EstoqueProdutos
    template_name = 'estoque/estoque_detail.html'
    context_object_name = 'estoqueprodutos'