from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Categoria, Produto
from .forms import CategoriaForm, ProdutoForm

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'produto/categoria_list.html'
    context_object_name = 'categorias'

class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'produto/categoria_form.html'
    success_url = reverse_lazy('produto:categoria_list')

class CategoriaUpdateView(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'produto/categoria_form.html'
    success_url = reverse_lazy('produto:categoria_list')

class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'produto/categoria_delete.html'
    success_url = reverse_lazy('produto:categoria_list')

class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'produto/categoria_detail.html'
    context_object_name = 'categoria'

class ProdutoListView(ListView):
    model = Produto
    template_name = 'produto/produto_list.html'
    context_object_name = 'produtos'

class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto/produto_form.html'
    success_url = reverse_lazy('produto:produto_list')

class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto/produto_form.html'
    success_url = reverse_lazy('produto:produto_list')

class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produto/produto_delete.html'
    success_url = reverse_lazy('produto:produto_list')

class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produto/produto_detail.html'
    context_object_name = 'produto'
