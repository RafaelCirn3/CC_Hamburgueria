from django.contrib import admin
from .models import Fornecedor, EstoqueProdutos

# Configuração para o modelo Fornecedor no Admin
@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'email', 'telefone')
    search_fields = ('nome', 'cnpj', 'email')
    list_filter = ('nome',)
    ordering = ('nome',)

# Configuração para o modelo EstoqueProdutos no Admin
@admin.register(EstoqueProdutos)
class EstoqueProdutosAdmin(admin.ModelAdmin):
    list_display = ('produto', 'fornecedor', 'quantidade', 'valor', 'data_criacao', 'data_atualizacao')
    search_fields = ('produto__nome', 'fornecedor__nome')
    list_filter = ('produto', 'fornecedor', 'data_criacao')
    ordering = ('-data_criacao',)
    autocomplete_fields = ('produto', 'fornecedor')
