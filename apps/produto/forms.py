from django.forms import ModelForm
from .models import Categoria, Produto


class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao']

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['categoria', 'nome', 'descricao', 'preco', 'fabricante', 'validade']
