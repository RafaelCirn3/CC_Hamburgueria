from django.urls import path
from .views import (
    PedidoCreate, PedidoUpdate, PedidoDelete, PedidoList, PedidoDetail,
    ItemPedidoCreate, ItemPedidoUpdate, ItemPedidoDelete, ItemPedidoList, ItemPedidoDetail
)

app_name = 'pedido'

urlpatterns = [
    path('', PedidoList.as_view(), name='pedido_list'),
    path('novo/', PedidoCreate.as_view(), name='pedido_create'),
    path('<int:pk>/editar/', PedidoUpdate.as_view(), name='pedido_update'),
    path('<int:pk>/excluir/', PedidoDelete.as_view(), name='pedido_delete'),
    path('<int:pk>/', PedidoDetail.as_view(), name='pedido_detail'),
    path('itempedido/', ItemPedidoList.as_view(), name='itempedido_list'),
    path('itempedido/novo/', ItemPedidoCreate.as_view(), name='itempedido_create'),
    path('itempedido/<int:pk>/editar/', ItemPedidoUpdate.as_view(), name='itempedido_update'),
    path('itempedido/<int:pk>/excluir/', ItemPedidoDelete.as_view(), name='itempedido_delete'),
    path('itempedido/<int:pk>/', ItemPedidoDetail.as_view(), name='itempedido_detail'),
]