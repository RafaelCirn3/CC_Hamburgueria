from django.urls import path
from .views import (
    FornecedorListView, FornecedorCreateView, FornecedorUpdateView, FornecedorDeleteView,
    EstoqueProdutosListView, EstoqueProdutosCreateView, EstoqueProdutosUpdateView, EstoqueProdutosDeleteView
)

app_name = 'estoque'

urlpatterns = [
    path('fornecedores/', FornecedorListView.as_view(), name='fornecedor_list'),
    path('fornecedores/novo/', FornecedorCreateView.as_view(), name='fornecedor_create'),
    path('fornecedores/<int:pk>/editar/', FornecedorUpdateView.as_view(), name='fornecedor_update'),
    path('fornecedores/<int:pk>/excluir/', FornecedorDeleteView.as_view(), name='fornecedor_delete'),
    path('estoqueprodutos/', EstoqueProdutosListView.as_view(), name='estoque_list'),
    path('estoqueprodutos/novo/', EstoqueProdutosCreateView.as_view(), name='estoque_create'),
    path('estoqueprodutos/<int:pk>/editar/', EstoqueProdutosUpdateView.as_view(), name='estoque_update'),
    path('estoqueprodutos/<int:pk>/excluir/', EstoqueProdutosDeleteView.as_view(), name='estoque_delete'),
]