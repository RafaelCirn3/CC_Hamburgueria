from .models import ItemPedido, Pedido
from django.forms import ModelForm

class ItemPedidoForm(ModelForm):
    class Meta:
        model = ItemPedido
        fields = ['produto', 'quantidade']

class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = ['comanda', 'itens']

class AddItemPedidoForm(ModelForm):
    class Meta:
        model = ItemPedido
        fields = ['produto', 'quantidade']
