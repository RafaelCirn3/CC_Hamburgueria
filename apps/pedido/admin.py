from django.contrib import admin
from .models import Pedido, ItemPedido

@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'quantidade')
    search_fields = ('produto__nome',)
    list_filter = ('produto',)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'comanda', 'criado', 'atualizado', 'total_pedido')
    search_fields = ('comanda__nome_cliente', 'comanda__mesa__numero')
    list_filter = ('criado', 'atualizado', 'comanda__mesa')
