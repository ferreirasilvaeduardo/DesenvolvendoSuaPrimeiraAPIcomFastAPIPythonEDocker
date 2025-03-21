# Store API Package

Este projeto é uma API desenvolvida com FastAPI utilizando a abordagem de Desenvolvimento Orientado a Testes (TDD). A API é voltada para gerenciar operações de uma loja, como produtos, pedidos e clientes.

## Funcionalidades

- Gerenciamento de produtos (CRUD)
- Gerenciamento de pedidos
- Gerenciamento de clientes
- Testes automatizados para garantir a qualidade do código

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto
- **FastAPI**: Framework para construção da API
- **Pytest**: Framework para testes
- **Uvicorn**: Servidor ASGI para rodar a aplicação

## Como Configurar o Projeto

1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd store-api-package
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute os testes para garantir que tudo está funcionando:
   ```bash
   pytest
   ```

5. Inicie o servidor:
   ```bash
   uvicorn main:app --reload
   ```

6. Acesse a documentação interativa da API em:
   ```
   http://127.0.0.1:8000/docs
   ```

## Estrutura do Projeto

Abaixo está a estrutura de diretórios do projeto:

```
store-api-package/
├── app/
│   ├── __init__.py
│   ├── main.py          # Ponto de entrada da aplicação
│   ├── api/             # Módulo para rotas da API
│   │   ├── __init__.py
│   │   ├── v1/          # Versão 1 das rotas
│   │   │   ├── __init__.py
│   │   │   ├── products.py  # Rotas relacionadas a produtos
│   │   │   └── users.py     # Rotas relacionadas a usuários
│   ├── core/            # Configurações centrais da aplicação
│   │   ├── __init__.py
│   │   ├── config.py    # Configurações gerais
│   │   └── security.py  # Configurações de segurança
│   ├── models/          # Modelos de dados
│   │   ├── __init__.py
│   │   ├── product.py   # Modelo de produto
│   │   └── user.py      # Modelo de usuário
│   ├── schemas/         # Schemas para validação
│   │   ├── __init__.py
│   │   ├── product.py   # Schema de produto
│   │   └── user.py      # Schema de usuário
│   └── services/        # Lógica de negócios
│       ├── __init__.py
│       ├── product_service.py  # Serviço para produtos
│       └── user_service.py     # Serviço para usuários
├── tests/
│   ├── __init__.py
│   ├── test_products.py # Testes para produtos
│   ├── test_users.py    # Testes para usuários
│   └── ...              # Outros testes
├── requirements.txt      # Dependências do projeto
└── README.md             # Documentação do projeto
```

## Contribuindo

Contribuições são bem-vindas! Siga os passos abaixo para contribuir:

1. Faça um fork do repositório.
2. Crie uma branch para sua feature ou correção:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça commit das suas alterações:
   ```bash
   git commit -m "Descrição da minha feature"
   ```
4. Envie para o repositório remoto:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
