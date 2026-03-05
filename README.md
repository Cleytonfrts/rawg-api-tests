# 🎮 RAWG API - Automação de Testes (QA)

Este projeto é um portfólio prático de Quality Assurance focado na automação de testes de backend (API REST). O objetivo é validar o comportamento, os contratos de dados e a segurança da **RAWG Video Games Database API**, aplicando boas práticas de engenharia de software e código limpo.

## 🛠️ Tecnologias Utilizadas

O projeto foi mantido enxuto, utilizando as bibliotecas essenciais para requisições e validações em Python:
- **Python 3**
- **Pytest** (Framework principal de testes e fixtures)
- **Requests** (Cliente HTTP)
- **python-dotenv** (Gerenciamento seguro de variáveis de ambiente)
- **Postman** (Mapeamento e testes manuais pré-automação)

## 🏗️ Arquitetura e Boas Práticas

A estrutura foi pensada para ser escalável e de fácil manutenção, separando as responsabilidades de conexão e de validação:

- `api/client.py`: Contém a classe `RawgClient`, responsável **apenas** por construir as requisições, tratar URLs e gerenciar timeouts. O cliente é agnóstico, ou seja, não sabe de onde vêm as credenciais.
- `tests/conftest.py`: Utiliza o conceito de injeção de dependência via Fixtures do Pytest para instanciar o cliente e entregá-lo configurado para os testes, validando o ambiente (*Fail Fast*).
- `tests/test_games.py`: Agrupa os testes em classes lógicas (`TestGamesSuccess` e `TestGamesErrors`), focando estritamente na regra de negócio e nas asserções.

## 🎯 Cenários Cobertos

Os testes atuais focam no endpoint `/games`:

1. **Caminho Feliz (Smoke Test):** Valida se a API responde corretamente (HTTP 200 OK) com credenciais válidas.
2. **Validação de Contrato (JSON Schema):** Garante que a estrutura da resposta contém os campos fundamentais esperados por um front-end (ex: `id`, `name`, `slug`, `released`, `rating`).
3. **Caminho Triste (Segurança):** Simula um cliente com API Key inválida e garante que o acesso seja barrado (HTTP 401 Unauthorized).

## 🚀 Como Executar o Projeto Localmente

Para rodar os testes na sua máquina, siga os passos abaixo:

### 1. Clone o repositório
```bash
git clone https://github.com/Cleytonfrts/rawg-api-tests
cd rawg-api-tests
```

### 2. Configure o Ambiente Virtual
Crie e ative um ambiente virtual (venv) para isolar as dependências:
- **Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
- **Linux/Mac:**
  ```bash
  python -m venv venv
  source venv/bin/activate
  ```

### 3. Instale as Dependências
```bash
pip install -r requirements.txt
```

### 4. Configure as Credenciais
Para interagir com a API, você precisará de uma chave (gratuita em [rawg.io/apidocs](https://rawg.io/apidocs)).
1. Crie um arquivo chamado `.env` na raiz do projeto.
2. Copie o conteúdo do arquivo `.env.example` para o seu `.env`.
3. Substitua o valor `inserir_chave_aqui` pela sua API Key real.

### 5. Execute os Testes
Com o ambiente configurado, rode o comando abaixo no terminal:
```bash
pytest -v
```

## 📂 Testes Manuais (Postman)

A automação foi precedida por testes exploratórios e mapeamento de contrato. Na pasta `postman/` deste repositório, você encontrará a Collection exportada e um README específico detalhando os cenários manuais validados.

## 👨‍💻 Autor

**Cleyton Freitas**