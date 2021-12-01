from rest_framework.test import APITestCase
from manager.models import Empresa
from django.urls import reverse
from rest_framework import status
from validate_docbr import CNPJ


class CursosTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse("Empresas-list")
        self.empresas = {
            "valida": {
                "nome_social": "Company Hero",
                "cnpj": 27961641000169
            },
            "invalida": {
                "nome_social": "OffShore DuGuedys",
                "cnpj": 333
            },
        }
        self.empresa_1 = Empresa.objects.create(
            cnpj=CNPJ().generate(),
            nome_social="EMPRESA FANTASMA"
        )
        self.empresa_2 = Empresa.objects.create(
            cnpj=CNPJ().generate(),
            nome_social="Kopenhagen"
        )

    def test_requisicao_get_para_listar_empresas(self):
        """Teste para verificar a requisição GET para listar as empresas"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_empresa_com_sucesso(self):
        """Teste para verificar a requisição POST para criar uma empresa"""
        data = {
            "nome_social": self.empresas['valida']['nome_social'],
            "cnpj": self.empresas['valida']['cnpj']
        }
        response = self.client.post(
            path=self.list_url,
            data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_post_para_criar_empresa_com_falha(self):
        """Teste para verificar a requisição POST para criar uma empresa"""
        data = {
            "nome_social": self.empresas['invalida']['nome_social'],
            "cnpj": self.empresas['invalida']['cnpj']
        }
        response = self.client.post(
            path=self.list_url,
            data=data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_requisicao_put_para_atualizar_empresa(self):
        """Teste para verificar a requisição PUT para atualizar uma empresa"""
        data = {
            "nome_social": self.empresas['valida']['nome_social'],
        }
        response = self.client.put("/empresas/1", data=data)
        self.assertEquals(response.status_code,
                          status.HTTP_301_MOVED_PERMANENTLY)

    def test_requisicao_delete_para_deletar_empresa(self):
        """Teste para verificar a requisição DELETE não permitida para deletar uma empresa"""
        response = self.client.delete("/empresas/1")
        self.assertEquals(response.status_code,
                          status.HTTP_301_MOVED_PERMANENTLY)
