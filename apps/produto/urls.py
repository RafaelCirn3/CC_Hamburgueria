from django.urls import path
from .views import CategoriaListView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView, CategoriaDetailView, ProdutoListView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView, ProdutoDetailView

app_name = 'produto'

urlpatterns = [
    path('categoria/', CategoriaListView.as_view(), name='categoria_list'),
    path('categoria/novo/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('categoria/<int:pk>/editar/', CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categoria/<int:pk>/excluir/', CategoriaDeleteView.as_view(), name='categoria_delete'),
    path('categoria/<int:pk>/', CategoriaDetailView.as_view(), name='categoria_detail'),
    path('produto/', ProdutoListView.as_view(), name='produto_list'),
    path('produto/novo/', ProdutoCreateView.as_view(), name='produto_create'),
    path('produto/<int:pk>/editar/', ProdutoUpdateView.as_view(), name='produto_update'),
    path('produto/<int:pk>/excluir/', ProdutoDeleteView.as_view(), name='produto_delete'),
    path('produto/<int:pk>/', ProdutoDetailView.as_view(), name='produto_detail'),
]