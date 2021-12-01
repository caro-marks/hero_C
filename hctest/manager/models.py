from django.db import models
from django.db.models.base import Model


class Empresa(models.Model):
    nome_social = models.CharField(max_length=120)
    cnpj = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.nome_social


class Funcionario(models.Model):
    primeiro_nome = models.CharField(max_length=30)
    ultimo_nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return f'{self.primeiro_nome} {self.ultimo_nome}'


class Contrato(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)
