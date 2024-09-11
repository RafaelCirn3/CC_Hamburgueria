from django.db import models


# Create your models here.
class Mesa(models.Model):
    numero = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Mesa"
        verbose_name_plural = "Mesas"

    def __str__(self):
        return f"Mesa: {self.numero}"


class Comanda(models.Model):
    class Situacao(models.TextChoices):
        ABERTO = "AB", "Aberto"
        FECHADO = "FE", "Fechado"

    nome_cliente = models.CharField(max_length=100)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, null=True, blank=True)
    situacao = models.CharField(
        max_length=2, choices=Situacao.choices, default=Situacao.ABERTO
    )
    custo = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Comanda"
        verbose_name_plural = "Comandas"

    def __str__(self):
        return f"Comanda: {self.mesa.numero} - {self.nome_cliente}"
