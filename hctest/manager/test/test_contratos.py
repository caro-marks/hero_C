from rest_framework.test import APITestCase
from manager.models import Contrato, Empresa, Funcionario
from django.urls import reverse
from rest_framework import status
from validate_docbr import CPF, CNPJ


class ContratosTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse("Contratos-list")
        self.contrato_1 = Contrato.objects.create(
            funcionario=Funcionario.objects.create(
                primeiro_nome="Laranjinha",
                ultimo_nome="Camarada",
                cpf=CPF().generate()
            ),
            empresa=Empresa.objects.create(
                cnpj=CNPJ().generate(),
                nome_social="EMPRESA FANTASMA"
            ),
        )
        self.contrato_2 = Contrato.objects.create(
            funcionario=Funcionario.objects.create(
                primeiro_nome="Fabricio",
                ultimo_nome="Queiroz",
                cpf=CPF().generate()
            ),
            empresa=Empresa.objects.create(
                cnpj=CNPJ().generate(),
                nome_social="Kopenhagen"
            ),)

    def test_requisicao_get_para_listar_contratos(self):
        """Teste para verificar a requisição GET para listar os contratos"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_put_para_atualizar_contrato(self):
        """Teste para verificar a requisição PUT para atualizar um contrato"""
        data = {
            "funcionario_id": 1,
            "empresa_id": 2,
        }
        response = self.client.put("/contratos/1/", data=data)
        self.assertEquals(response.status_code,
                          status.HTTP_405_METHOD_NOT_ALLOWED)
