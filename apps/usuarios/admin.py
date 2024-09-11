from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    # O modelo que será utilizado
    model = Usuario

    # Exibição dos campos na lista de usuários
    list_display = ('email', 'first_name', 'last_name', 'cpf', 'telefone', 'cargo', 'is_staff')

    # Filtros laterais para pesquisa rápida
    list_filter = ('cargo', 'is_staff', 'is_superuser', 'is_active')

    # Permite a busca por campos como email, nome, sobrenome e CPF
    search_fields = ('email', 'first_name', 'last_name', 'cpf')

    # Ordenação da lista de usuários
    ordering = ('email',)

    # Campos que serão exibidos no formulário de edição do usuário
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações pessoais', {'fields': ('first_name', 'last_name', 'cpf', 'telefone')}),
        ('Cargo', {'fields': ('cargo',)}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
    )

    # Campos que aparecerão ao adicionar um novo usuário
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'cpf', 'telefone', 'cargo', 'password1', 'password2'),
        }),
    )

