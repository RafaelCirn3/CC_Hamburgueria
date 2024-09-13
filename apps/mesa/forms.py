from django.forms import ModelForm
from apps.mesa.models import Mesa, Comanda
"""construir o forms para os templates de mesa"""


class MesaForm(ModelForm):
    class Meta:
        model = Mesa
        fields = ['numero', 'disponivel']

class ComandaForm(ModelForm):
    class Meta:
        model = Comanda
        fields = ['nome_cliente', 'mesa', 'situacao', 'custo']