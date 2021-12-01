from manager.models import Contrato
from validate_docbr import CPF, CNPJ


def cpf_valido(cpf):
    return CPF().validate(cpf)


def cnpj_valido(cnpj):
    return CNPJ().validate(cnpj)


def funcionario_valido(id):
    return len(Contrato.objects.filter(funcionario_id=id)) > 0


def empresa_valida(id):
    return len(Contrato.objects.filter(empresa_id=id)) > 0
