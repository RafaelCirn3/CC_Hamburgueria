from django.urls import path
from .views import (
    MesaListView, MesaCreateView, MesaUpdateView, MesaDeleteView, MesaDetailView,
    ComandaListView, ComandaCreateView, ComandaUpdateView, ComandaDeleteView, ComandaDetailView
)

app_name = 'mesa'

urlpatterns = [
    path('mesas/', MesaListView.as_view(), name='mesa_list'),
    path('mesas/novo/', MesaCreateView.as_view(), name='mesa_create'),
    path('mesas/<int:pk>/editar/', MesaUpdateView.as_view(), name='mesa_update'),
    path('mesas/<int:pk>/excluir/', MesaDeleteView.as_view(), name='mesa_delete'),
    path('mesas/<int:pk>/', MesaDetailView.as_view(), name='mesa_detail'),
    path('comandas/', ComandaListView.as_view(), name='comanda_list'),
    path('comandas/novo/', ComandaCreateView.as_view(), name='comanda_create'),
    path('comandas/<int:pk>/editar/', ComandaUpdateView.as_view(), name='comanda_update'),
    path('comandas/<int:pk>/excluir/', ComandaDeleteView.as_view(), name='comanda_delete'),
    path('comandas/<int:pk>/', ComandaDetailView.as_view(), name='comanda_detail'),
]
