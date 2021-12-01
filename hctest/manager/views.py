from rest_framework.exceptions import NotFound
from rest_framework import generics, viewsets, filters
from manager.models import Contrato, Empresa, Funcionario
from manager.serializers import ContratoSerializer, ContratosEmpresaSerializer, ContratosFuncionarioSerializer, EmpresaSerializer, FuncionarioSerializer


class EmpresaViewSet(viewsets.ModelViewSet):
    """ Exibe todas as empresas """
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['nome_social']


class FuncionarioViewSet(viewsets.ModelViewSet):
    """ Exibe todos os funcionarios """
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['primeiro_nome', 'ultimo_nome']


class ContratoViewSet(viewsets.ModelViewSet):
    """ Exibe todos os contratos """
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer
    filter_backends = [filters.OrderingFilter]
    filterset_fields = ['ativo']


class ContratosFuncionarioListView(generics.ListAPIView):
    def get_queryset(self):
        queryset = Contrato.objects.filter(funcionario_id=self.kwargs['pk'])
        if len(queryset) == 0:
            raise NotFound({'funcionario': 'inexistente.'})
        return queryset

    serializer_class = ContratosFuncionarioSerializer


class ContratosEmpresaListView(generics.ListAPIView):
    def get_queryset(self):
        queryset = Contrato.objects.filter(empresa_id=self.kwargs['pk'])
        if len(queryset) == 0:
            raise NotFound({'empresa': 'inexistente'})
        return queryset

    serializer_class = ContratosEmpresaSerializer
