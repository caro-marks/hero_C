from rest_framework.test import APITestCase
from manager.models import Funcionario
from django.urls import reverse
from rest_framework import status
from validate_docbr import CPF


class FuncionariosTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse("Funcionarios-list")
        self.funcionarios = {
            "valido": {
                "primeiro_nome": "Ronaldo",
                "ultimo_nome": "Fenômeno",
                "cpf": CPF().generate()
            },
            "invalido": {
                "primeiro_nome": "Presidanta",
                "ultimo_nome": "Mitoverso",
                "cpf": 666
            },
        }
        self.funcionario_1 = Funcionario.objects.create(
            primeiro_nome="Laranjinha",
            ultimo_nome="Camarada",
            cpf=CPF().generate()
        )
        self.funcionario_2 = Funcionario.objects.create(
            primeiro_nome="Fabricio",
            ultimo_nome="Queiroz",
            cpf=CPF().generate()
        )

    def test_requisicao_get_para_listar_funcionarios(self):
        """Teste para verificar a requisição GET para listar os funcionarios"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_funcionario_com_sucesso(self):
        """Teste para verificar a requisição POST para criar um funcionario"""
        data = {
            "primeiro_nome": self.funcionarios['valido']['primeiro_nome'],
            "ultimo_nome": self.funcionarios['valido']['ultimo_nome'],
            "cpf": self.funcionarios['valido']['cpf']
        }
        response = self.client.post(
            path=self.list_url,
            data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_post_para_criar_funcionario_com_falha(self):
        """Teste para verificar a requisição POST para criar um funcionario"""
        data = {
            "primeiro_nome": self.funcionarios['invalido']['primeiro_nome'],
            "ultimo_nome": self.funcionarios['invalido']['ultimo_nome'],
            "cpf": self.funcionarios['invalido']['cpf']
        }
        response = self.client.post(
            path=self.list_url,
            data=data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_requisicao_put_para_atualizar_funcionario(self):
        """Teste para verificar a requisição PUT para atualizar um funcionario"""
        data = {
            "primeiro_nome": self.funcionarios['invalido']['primeiro_nome'],
            "ultimo_nome": self.funcionarios['valido']['ultimo_nome']
        }
        response = self.client.put("/funcionarios/1", data=data)
        self.assertEquals(response.status_code,
                          status.HTTP_301_MOVED_PERMANENTLY)

    def test_requisicao_delete_para_deletar_funcionario(self):
        """Teste para verificar a requisição DELETE não permitida para deletar um funcionario"""
        response = self.client.delete("/funcionarios/1")
        self.assertEquals(response.status_code,
                          status.HTTP_301_MOVED_PERMANENTLY)
