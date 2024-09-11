from apps.produto.models import Produto
from apps.mesa.models import Comanda
from django.db import models

class ItemPedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    class Meta:
        verbose_name = "Item do Pedido"
        verbose_name_plural = "Itens do Pedido"

    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade}"


class Pedido(models.Model):
    comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE)
    itens = models.ManyToManyField(ItemPedido)  # Alterado de 'items' para 'itens'
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def __str__(self):
        return f"Pedido {self.id} - Mesa: {self.comanda.mesa.numero}, Cliente: {self.comanda.nome_cliente}"

    def total_pedido(self):
        """Calcula o valor total do pedido com base na quantidade e preço dos itens"""
        total = sum(item.produto.preco * item.quantidade for item in self.itens.all())
        return total
