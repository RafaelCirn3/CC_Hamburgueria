from django.contrib import admin
from .models import Mesa, Comanda

@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'disponivel', 'data_criacao', 'data_atualizacao')  # Exibe as colunas da lista
    list_filter = ('disponivel',)  # Filtros laterais por disponibilidade
    search_fields = ('numero',)  # Permite busca por número da mesa
    ordering = ('numero',)  # Ordena a lista de mesas pelo número

@admin.register(Comanda)
class ComandaAdmin(admin.ModelAdmin):
    list_display = ('nome_cliente', 'mesa', 'situacao', 'data_criacao', 'data_atualizacao')  # Exibe nome do cliente, mesa e situação
    list_filter = ('situacao', 'mesa')  # Filtros laterais por situação e mesa
    search_fields = ('nome_cliente', 'mesa__numero')  # Permite busca por nome do cliente e número da mesa
    ordering = ('mesa', 'nome_cliente')  # Ordena por mesa e nome do cliente
