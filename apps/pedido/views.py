from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.db import transaction
from .models import ItemPedido, Pedido
from .forms import ItemPedidoForm, PedidoForm
class PedidoCreate(CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'pedido/pedido_form.html'
    success_url = reverse_lazy('pedido:pedido_list')
    
    def form_valid(self, form):
        with transaction.atomic():
            pedido = form.save()
            # Verificar estoque de cada item antes de confirmar o pedido
            for item in pedido.itens.all():
                if item.produto.estoque < item.quantidade:
                    form.add_error(None, f"Estoque insuficiente para o produto {item.produto.nome}")
                    return self.form_invalid(form)
                # Atualizar o estoque
                item.produto.estoque -= item.quantidade
                item.produto.save()
        return super().form_valid(form)

class PedidoUpdate(UpdateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'pedido/pedido_form.html'
    success_url = reverse_lazy('pedido:pedido_list')
    def form_valid(self, form):
        with transaction.atomic():
            pedido_antigo = Pedido.objects.get(pk=self.object.pk)
            # Reverter o estoque antes de salvar o pedido atualizado
            for item in pedido_antigo.itens.all():
                item.produto.estoque += item.quantidade
                item.produto.save()
            pedido = form.save()
            # Verificar estoque e atualizar com base no novo pedido
            for item in pedido.itens.all():
                if item.produto.estoque < item.quantidade:
                    form.add_error(None, f"O produto {item.produto.nome} não possui estoque suficiente.")
                    return super().form_invalid(form)
                item.produto.estoque -= item.quantidade
                item.produto.save()
        return super().form_valid(form)
class PedidoDelete(DeleteView):
    model = Pedido
    template_name = 'pedido/pedido_delete.html'
    success_url = reverse_lazy('pedido:pedido_list')
    def delete(self, request, *args, **kwargs):
        pedido = self.get_object()
        with transaction.atomic():
            # Reverter estoque antes de deletar o pedido
            for item in pedido.itens.all():
                item.produto.estoque += item.quantidade
                item.produto.save()
        return super().delete(request, *args, **kwargs)
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

    def form_valid(self, form):
        itempedido = form.save(commit=False)
        # verifica se o produto tem estoque suficiente
        if itempedido.produto.estoque < itempedido.quantidade:
            form.add_error(None, f"O produto {itempedido.produto.nome} não possui estoque suficiente.")
            return super().form_invalid(form)
        # tira o produto do estoque
        itempedido.produto.estoque -= itempedido.quantidade
        itempedido.produto.save()
        return super().form_valid(form)
class ItemPedidoUpdate(UpdateView):
    model = ItemPedido
    form_class = ItemPedidoForm
    template_name = 'pedido/itempedido_form.html'
    success_url = reverse_lazy('pedido:itempedido_list')

    def form_valid(self, form):
        itempedido_antigo = ItemPedido.objects.get(pk=self.object.pk)
        # Reverter o estoque antigo antes de atualizar
        itempedido_antigo.produto.estoque += itempedido_antigo.quantidade
        itempedido_antigo.produto.save()

        itempedido = form.save(commit=False)
        # Verificar estoque antes de confirmar a atualização
        if itempedido.produto.estoque < itempedido.quantidade:
            form.add_error(None, f"Estoque insuficiente para o produto {itempedido.produto.nome}")
            return super().form_invalid(form)
        # Atualizar o estoque
        itempedido.produto.estoque -= itempedido.quantidade
        itempedido.produto.save()
        return super().form_valid(form)
class ItemPedidoDelete(DeleteView):
    model = ItemPedido
    template_name = 'pedido/itempedido_delete.html'
    success_url = reverse_lazy('pedido:itempedido_list')

    def delete(self, request, *args, **kwargs):
        itempedido = self.get_object()
        # Reverter o estoque quando um item de pedido for excluído
        itempedido.produto.estoque += itempedido.quantidade
        itempedido.produto.save()
        return super().delete(request, *args, **kwargs)
class ItemPedidoList(ListView):
    model = ItemPedido
    template_name = 'pedido/itempedido_list.html'
    context_object_name = 'itenspedido'

class ItemPedidoDetail(DetailView):
    model = ItemPedido
    template_name = 'pedido/itempedido_detail.html'
    context_object_name = 'itempedido'

