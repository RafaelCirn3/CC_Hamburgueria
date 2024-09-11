from django.contrib.auth.models import AbstractUser
from tools.CustomFields.Phone import BRPhoneField
from tools.CustomFields.Identity import CPFField
from .managers import UsuarioManager
from django.db import models


class Usuario(AbstractUser):
    class Cargos(models.TextChoices):
        ADMIN = "ADM", "Administrador"
        FUNCIONARIO = "FUN", "Funcionário"

    email = models.EmailField(unique=True)
    first_name = models.CharField("Primeiro Nome", max_length=30)
    last_name = models.CharField("Sobrenome",max_length=150)
    cpf = CPFField(unique=True)
    telefone = BRPhoneField()
    cargo = models.CharField(
        max_length=3, choices=Cargos.choices, default=Cargos.FUNCIONARIO
    )

    USERNAME_FIELD = "email"  # Define o email como o campo de login
    REQUIRED_FIELDS = [
        "cpf",
        "telefone",
        "first_name",
        "last_name",
    ]  # Campos obrigatórios além do email

    objects = UsuarioManager()  # Define o manager customizado

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return f"{self.email} - {self.cpf}"
