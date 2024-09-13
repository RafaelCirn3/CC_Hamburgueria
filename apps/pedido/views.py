from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import ItemPedido, Pedido
from .forms import ItemPedidoForm, PedidoForm
class PedidoCreate(CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'pedido/pedido_form.html'
    success_url = reverse_lazy('pedido:pedido_list')

class PedidoUpdate(UpdateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'pedido/pedido_form.html'
    success_url = reverse_lazy('pedido:pedido_list')
    
class PedidoDelete(DeleteView):
    model = Pedido
    template_name = 'pedido/pedido_delete.html'
    success_url = reverse_lazy('pedido:pedido_list')

class PedidoList(ListView):
    model = Pedido
    template_name = 'pedido/pedido_list.html'
    context_object_name = 'pedidos'

class PedidoDetail(DetailView):
    model = Pedido
    template_name = 'pedido/pedido_detail.html'
    context_object_name = 'pedido'

class ItemPedidoCreate(CreateView):
    model = ItemPedido
    form_class = ItemPedidoForm
    template_name = 'pedido/itempedido_form.html'
    success_url = reverse_lazy('pedido:itempedido_list')

class ItemPedidoUpdate(UpdateView):
    model = ItemPedido
    form_class = ItemPedidoForm
    template_name = 'pedido/itempedido_form.html'
    success_url = reverse_lazy('pedido:itempedido_list')

class ItemPedidoDelete(DeleteView):
    model = ItemPedido
    template_name = 'pedido/itempedido_delete.html'
    success_url = reverse_lazy('pedido:itempedido_list')

class ItemPedidoList(ListView):
    model = ItemPedido
    template_name = 'pedido/itempedido_list.html'
    context_object_name = 'itenspedido'

class ItemPedidoDetail(DetailView):
    model = ItemPedido
    template_name = 'pedido/itempedido_detail.html'
    context_object_name = 'itempedido'

