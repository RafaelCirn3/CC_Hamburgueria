from django.urls import path
from .views import (
    FornecedorListView, FornecedorCreateView, FornecedorUpdateView, FornecedorDeleteView, FornecedorDetailView,
    EstoqueProdutosListView, EstoqueProdutosCreateView, EstoqueProdutosUpdateView, EstoqueProdutosDeleteView, EstoqueProdutosDetailView
)

app_name = 'estoque'

urlpatterns = [
    path('fornecedores/', FornecedorListView.as_view(), name='fornecedor_list'),
    path('fornecedores/novo/', FornecedorCreateView.as_view(), name='fornecedor_create'),
    path('fornecedores/<int:pk>/editar/', FornecedorUpdateView.as_view(), name='fornecedor_update'),
    path('fornecedores/<int:pk>/excluir/', FornecedorDeleteView.as_view(), name='fornecedor_delete'),
    path('fornecedores/<int:pk>/', FornecedorDetailView.as_view(), name='fornecedor_detail'),
    path('estoque/', EstoqueProdutosListView.as_view(), name='estoque_list'),
    path('estoque/novo/', EstoqueProdutosCreateView.as_view(), name='estoque_create'),
    path('estoque/<int:pk>/editar/', EstoqueProdutosUpdateView.as_view(), name='estoque_update'),
    path('estoque/<int:pk>/excluir/', EstoqueProdutosDeleteView.as_view(), name='estoque_delete'),
    path('estoque/<int:pk>/', EstoqueProdutosDetailView.as_view(), name='estoque_detail'),
]