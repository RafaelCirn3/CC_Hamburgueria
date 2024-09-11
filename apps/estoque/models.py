from django.db import models
from apps.produto.models import Produto
# Create your models here.

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    telefone = models.CharField(max_length=15,blank=True,null=True)

    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"
    
    def __str__(self):
        return f"Fornecedor: {self.nome}"

class EstoqueProdutos(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    

    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Estoque de Produto"
        verbose_name_plural = "Estoque de Produtos"

    def __str__(self):
        return f"Estoque de {self.produto.nome}"