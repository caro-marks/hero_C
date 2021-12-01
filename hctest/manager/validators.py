from manager.models import Contrato
from validate_docbr import CPF, CNPJ


def cpf_valido(cpf):
    return CPF().validate(cpf)


def cnpj_valido(cnpj):
    return CNPJ().validate(cnpj)


def funcionario_valido(contratos):
    return len(contratos) > 0


def empresa_valida(contratos):
    return len(contratos) > 0
