from django.forms import ModelForm
from apps.estoque.models import Fornecedor, EstoqueProdutos
"""construir o forms para os templates de estoque"""

class FornecedorForm(ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome', 'cnpj', 'email', 'telefone']

class EstoqueProdutosForm(ModelForm):
    class Meta:
        model = EstoqueProdutos
        fields = ['fornecedor', 'produto', 'quantidade', 'valor']