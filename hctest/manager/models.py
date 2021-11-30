from django.db import models


class Empresa(models.Model):
    nome_social = models.CharField(max_length=120)
    cnpj = models.CharField(max_length=14)

    def __str__(self):
        return f'empresa {self.nome_social}'


class Funcionario(models.Model):
    primeiro_nome = models.CharField(max_length=30)
    ultimo_nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11)
    trabalha_em = models.ManyToManyField(Empresa)

    def __str__(self):
        return f'funcionario {self.primeiro_nome} {self.ultimo_nome}'
