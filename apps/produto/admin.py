from django.contrib import admin
from .models import Categoria, Produto

# Configuração para o modelo Categoria no Admin
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'data_criacao', 'data_atualizacao')
    search_fields = ('nome',)
    list_filter = ('data_criacao', 'data_atualizacao')
    ordering = ('-data_criacao',)

# Configuração para o modelo Produto no Admin
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'preco', 'fabricante', 'validade')
    search_fields = ('nome', 'fabricante')
    list_filter = ('categoria', 'validade', 'preco')
    ordering = ('-validade',)
    autocomplete_fields = ('categoria',)
