from django.db.models import query
from rest_framework import serializers, viewsets
from manager.models import Empresa, Funcionario
from manager.serializers import EmpresaSerializer, FuncionarioSerializer


class EmpresaViewSet(viewsets.ModelViewSet):
    """ Exibe todas as empresas """
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer


class FuncionarioViewSet(viewsets.ModelViewSet):
    """ Exibe todos os funcionarios """
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
