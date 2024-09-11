from django.core.exceptions import ValidationError
from django.db import models
from django import forms

class BRPhoneField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 13  # Com +55 pode ter até 13 caracteres (incluindo o +)
        kwargs['validators'] = [self.validate_phone]
        super(BRPhoneField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': forms.CharField}  # Formulário base
        defaults.update(kwargs)
        return super(BRPhoneField, self).formfield(**defaults)

    @staticmethod
    def validate_phone(value: str):
        if not value:
            return value

        # Remove todos os caracteres não numéricos
        value = ''.join(filter(str.isdigit, value))
        
        # Verifica se o telefone tem o tamanho esperado (DDD + número)
        if len(value) not in [11, 12]:  # Aceita 11 dígitos (8398946959) ou 12 (083998946959)
            raise ValidationError('Número de telefone deve ter 11 ou 12 dígitos.')

        # Verifica se o telefone tem DDD válido e começa com o dígito 9
        if len(value) == 11:  # Sem código de país
            if value[2] != '9':
                raise ValidationError('Número de telefone inválido, deve começar com o dígito 9 após o DDD.')

        elif len(value) == 12:  # Com código de país
            if value[2] != '9':
                raise ValidationError('Número de telefone inválido, deve começar com o dígito 9 após o DDD.')

        # Formata o número para incluir o código de país se necessário
        if len(value) == 11:
            value = f'+55{value}'

        return value
    
    

        
        

