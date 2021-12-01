from django.contrib import admin
from manager.models import Contrato, Empresa, Funcionario


class Empresas(admin.ModelAdmin):
    list_display = ('id', 'nome_social', 'cnpj')
    list_display_links = ('id', 'cnpj')
    search_fields = ('cnpj', )


admin.site.register(Empresa, Empresas)


class Funcionarios(admin.ModelAdmin):
    list_display = ('id', 'primeiro_nome', 'ultimo_nome', 'cpf')
    list_display_links = ('id', 'cpf')
    search_fields = ('cpf', )
    list_per_page = 25
    ordering = ('primeiro_nome', 'ultimo_nome')


admin.site.register(Funcionario, Funcionarios)


class Contratos(admin.ModelAdmin):
    list_display = ('id', 'funcionario', 'empresa')
    list_display_links = ('id', )
    search_fields = ('funcionario', 'empresa')


admin.site.register(Contrato, Contratos)