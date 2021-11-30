from django.db.models import fields
from rest_framework import serializers
from manager.models import Empresa, Funcionario


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'


class FuncionarioSerializer(serializers.ModelSerializer):
    class meta:
        model = Funcionario
        fields = '__all__'
