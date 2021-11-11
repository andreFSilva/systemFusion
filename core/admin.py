from django.contrib import admin
from .models import Servico, Funcionarios, Profissao, Clientes, Produtos


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificados')


@admin.register(Profissao)
class ProfissaoAdmin(admin.ModelAdmin):
    list_display = ('profissao', 'ativo', 'modificados')


@admin.register(Funcionarios)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'profissao', 'ativo', 'modificados')


@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'profissao', 'ativo', 'modificados')


@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'valor', 'ativo', 'modificados')