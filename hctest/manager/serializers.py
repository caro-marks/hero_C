from rest_framework import serializers
from manager.models import Contrato, Empresa, Funcionario
from manager import validators


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = (
            'nome_social',
            'cnpj',
        )

    def validate(self, data):
        if not validators.cnpj_valido(data['cnpj']):
            raise serializers.ValidationError(
                {'cnpj': 'Número de CNPJ inválido.'})
        return data


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'

    def validate(self, data):
        if not validators.cpf_valido(data['cpf']):
            raise serializers.ValidationError(
                {'cpf': 'Número de CPF inválido.'})
        return data


class ContratoSerializer(serializers.ModelSerializer):
    empresa = EmpresaSerializer()
    funcionario = FuncionarioSerializer()

    class Meta:
        model = Contrato
        exclude = []


class ContratosFuncionarioSerializer(serializers.ModelSerializer):
    empresa = EmpresaSerializer()

    class Meta:
        model = Contrato
        fields = [
            'empresa',
        ]


class ContratosEmpresaSerializer(serializers.ModelSerializer):
    funcionario = FuncionarioSerializer()

    class Meta:
        model = Contrato
        fields = ['funcionario']