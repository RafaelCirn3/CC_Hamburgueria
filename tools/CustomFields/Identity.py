from django.core.exceptions import ValidationError
from django.db import models
from django import forms


class CPFField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 11  # O tamanho máximo do CPF deve ser 11
        super(CPFField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        # Usa o forms.CharField, que pode ser substituído, se necessário
        defaults = {
            "form_class": forms.CharField
        }
        defaults.update(kwargs)
        return super(CPFField, self).formfield(**defaults)

    def clean(self, value, model_instance):
        value = super(CPFField, self).clean(value, model_instance)
        return self.validate_cpf(value)

    def validate_cpf(self, cpf):
        # Remove qualquer caractere não numérico
        cpf = "".join(filter(str.isdigit, cpf))

        # Verifica se o CPF tem 11 dígitos
        if len(cpf) != 11:
            raise ValidationError("O CPF deve ter 11 dígitos.", code="invalid")

        # Verifica se o CPF é composto por números repetidos (ex: 11111111111)
        if cpf == cpf[0] * len(cpf):
            raise ValidationError(
                "CPF inválido. Números repetidos não são permitidos.", code="invalid"
            )

        # Valida o primeiro dígito verificador
        soma_primeiro_digito = sum(int(cpf[i]) * (10 - i) for i in range(9))
        primeiro_digito_verificador = (soma_primeiro_digito * 10) % 11
        if primeiro_digito_verificador == 10:
            primeiro_digito_verificador = 0
        if primeiro_digito_verificador != int(cpf[9]):
            raise ValidationError(
                "CPF inválido. O primeiro dígito verificador não confere.",
                code="invalid",
            )

        # Valida o segundo dígito verificador
        soma_segundo_digito = sum(int(cpf[i]) * (11 - i) for i in range(10))
        segundo_digito_verificador = (soma_segundo_digito * 10) % 11
        if segundo_digito_verificador == 10:
            segundo_digito_verificador = 0
        if segundo_digito_verificador != int(cpf[10]):
            raise ValidationError(
                "CPF inválido. O segundo dígito verificador não confere.",
                code="invalid",
            )

        return cpf


class CNPJField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 14
        kwargs["validators"] = [self.validate_cnpj]
        super(CNPJField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            "form_class": forms.CharField
        }  # Você pode criar um campo de formulário customizado se necessário
        defaults.update(kwargs)
        return super(CNPJField, self).formfield(**defaults)

    def validate_cnpj(self, cnpj):
        # Remove qualquer caractere não numérico
        cnpj = "".join(filter(str.isdigit, cnpj))

        # Verifica se o CNPJ tem 14 dígitos
        if len(cnpj) != 14:
            raise ValidationError("O CNPJ deve ter 14 dígitos.", code="invalid")

        # Verifica se o CNPJ é composto por números repetidos (ex: 11111111111111)
        if cnpj == cnpj[0] * len(cnpj):
            raise ValidationError(
                "CNPJ inválido. Números repetidos não são permitidos.", code="invalid"
            )

        # Valida o primeiro dígito verificador
        pesos_primeiro = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        soma_primeiro_digito = sum(int(cnpj[i]) * pesos_primeiro[i] for i in range(12))
        primeiro_digito_verificador = (soma_primeiro_digito * 10) % 11
        if primeiro_digito_verificador == 10 or primeiro_digito_verificador == 11:
            primeiro_digito_verificador = 0
        if primeiro_digito_verificador != int(cnpj[12]):
            raise ValidationError(
                "CNPJ inválido. O primeiro dígito verificador não confere.",
                code="invalid",
            )

        # Valida o segundo dígito verificador
        pesos_segundo = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        soma_segundo_digito = sum(int(cnpj[i]) * pesos_segundo[i] for i in range(13))
        segundo_digito_verificador = (soma_segundo_digito * 10) % 11
        if segundo_digito_verificador == 10 or segundo_digito_verificador == 11:
            segundo_digito_verificador = 0
        if segundo_digito_verificador != int(cnpj[13]):
            raise ValidationError(
                "CNPJ inválido. O segundo dígito verificador não confere.",
                code="invalid",
            )

        return cnpj
