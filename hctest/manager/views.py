from rest_framework.exceptions import NotFound
from rest_framework import generics, viewsets, filters, mixins
from rest_framework.response import Response
from manager.validators import empresa_valida, funcionario_valido
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


class ContratoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin, mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    """ Exibe todos os contratos """
    queryset = Contrato.objects.filter(ativo=True)
    serializer_class = ContratoSerializer
    filter_backends = [filters.OrderingFilter]
    filterset_fields = ['ativo']

    def destroy(self, request, *args, **extra_args):
        contrato = self.get_object()
        contrato.ativo = False
        contrato.save()
        return Response(
            data={'SOFT DELETE': 'Contrato desativado com sucesso!'})


class ContratosFuncionarioListView(generics.ListAPIView):
    def get_queryset(self):
        queryset = Contrato.objects.filter(funcionario__cpf=self.kwargs['pk'])
        if not funcionario_valido(queryset):
            raise NotFound({'funcionario': 'inexistente.'})
        return queryset

    serializer_class = ContratosFuncionarioSerializer


class ContratosEmpresaListView(generics.ListAPIView):
    def get_queryset(self):
        queryset = Contrato.objects.filter(empresa_id=self.kwargs['pk'])
        if not empresa_valida(queryset):
            raise NotFound({'empresa': 'inexistente'})
        return queryset

    serializer_class = ContratosEmpresaSerializer
