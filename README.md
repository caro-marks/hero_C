<h1 align='center'> Company Hero Test </h1>
<p align='center'> Servidor que gerencia cadastro de funcionários, empresas, e contratos entre estes. </p>

### 🛠 Tecnologias

As ferramentas usadas na construção do projeto foi:

- **[Django](https://www.djangoproject.com/)**
- **[Django REST](https://www.django-rest-framework.org//nuxtjs.org/)**
- **[Docker](https://www.docker.com/)**

<h4 align='center'> 
	 🚀 Disponível no link https://ch-test-deploy.herokuapp.com/
</h4>

## Instruções para testar a aplicação localmente

### Clone este repositório

```
git clone https://github.com/caro-marks/hero_C.git ./
```

### Configure as variáveis de ambiente

```
cp .env.sample .env
cp ./hctest/.env.sample ./hctest/.env
```

### Subir Containers e Rodar a aplicação com MAKEFILE

```
make migrate
make build
```

## Documentação básica

### Funcionários

<strong>Objeto</strong> = {
"primeiro_nome": _nome_,
"ultimo_nome": _sobrenome_,
"cpf": _cpf válido_
}

| Método | Descrição                         | Url                  |
| ------ | --------------------------------- | -------------------- |
| GET    | Listar todos os funcionários      | /funcionarios/       |
| GET    | Listar um funcionário por seu id  | /funcionarios/_{id}_ |
| POST   | Cadastrar um funcionário          | /funcionarios/       |
| PUT    | Alterar um funcionário por seu id | /funcionarios/_{id}_ |
| DELETE | Deletar um funcionário por seu id | /funcionarios/_{id}_ |

### Empresas

<strong>Objeto</strong> = {
"nome_social": _nome da empresa_,
"cnpj": _cnpj válido_
}

| Método | Descrição                      | Url              |
| ------ | ------------------------------ | ---------------- |
| GET    | Listar todas as empresas       | /empresas/       |
| GET    | Listar uma empresa por seu id  | /empresas/_{id}_ |
| POST   | Cadastrar uma empresa          | /empresas/       |
| PUT    | Alterar uma empresa por seu id | /empresas/_{id}_ |
| DELETE | Deletar uma empresa por seu id | /empresas/_{id}_ |

### Contratos

<strong>Objeto</strong> = {
"funcionario": _id de funcionário_,
"empresa": _id de empresa_,
"ativo": \*Booleano"
}

_Não é possível alterar um contrato. O método HTTP DELETE é SOFT: o contrato não é excluido do banco de dados, somente desativado._

| Método | Descrição                      | Url               |
| ------ | ------------------------------ | ----------------- |
| GET    | Listar todos os contratos      | /contratos/       |
| GET    | Listar um contrato por seu id  | /contratos/_{id}_ |
| POST   | Cadastrar um contrato          | /contratos/       |
| DELETE | Deletar um contrato por seu id | /contratos/_{id}_ |

### Listas

| Método | Descrição                                                | Url                             |
| ------ | -------------------------------------------------------- | ------------------------------- |
| GET    | Listar todos os funcionários de uma empresa por seu CNPJ | /empresa/_{CNPJ}_/contratos/    |
| GET    | Listar todos os contratos de um funcionários por seu CPF | /funcionario/_{CPF}_/contratos/ |

#

### <a>🚀Feito por</a>

<a href="https://www.linkedin.com/in/caro-marks">
   <b>Marcos Nolasco</b> 👋🏽
</a>

---
