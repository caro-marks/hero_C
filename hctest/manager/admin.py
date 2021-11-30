from django.contrib import admin
from manager.models import Empresa, Funcionario


class Empresas(admin.ModelAdmin):
    list_display = ('id', 'nome_social', 'cnpj')
    list_display_links = ('id', 'cnpj')
    search_fields = ('cnpj', )


admin.site.register(Empresas)


class Funcionarios(admin.ModelAdmin):
    list_display = ('id', 'primeiro_nome', 'ultimo_nome', 'cpf', 'trabalha_em')
    list_display_links = ('id', 'cpf')
    search_fields = ('cpf', )
    list_per_page = 25


admin.site.register(Funcionarios)