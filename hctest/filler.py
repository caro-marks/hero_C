import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF, CNPJ
from random import randint, choice
from manager import models

fake = Faker('pt_BR')
Faker.seed(88)


def criando_empresas(quantidade):
    for _ in range(quantidade):
        cnpj = CNPJ().generate()
        nome_social = fake.company()
        e = models.Empresa(nome_social=nome_social, cnpj=cnpj)
        e.save()
        print(f'empresa {e.id} - {nome_social}')


def cadastrando_funcionarios(quantidade):
    for _ in range(quantidade):
        cpf = CPF()
        primeiro_nome = fake.first_name()
        ultimo_nome = fake.last_name()
        cpf = cpf.generate()
        f = models.Funcionario(primeiro_nome=primeiro_nome,
                               ultimo_nome=ultimo_nome,
                               cpf=cpf)
        f.save()
        print(f'funcionario {f.id} - {primeiro_nome} {ultimo_nome}')


def fazendo_contratos(quantidade):
    for _ in range(quantidade):
        c = models.Contrato.objects.get_or_create(funcionario_id=randint(
            1, 49),
                                                  empresa_id=randint(1, 24),
                                                  ativo=choice([True, False]))
        print(f'contrato {c[0].id}')


criando_empresas(25)
cadastrando_funcionarios(50)
fazendo_contratos(200)
print('Sucesso!')