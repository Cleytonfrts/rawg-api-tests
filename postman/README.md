# Testes Manuais - RAWG API

Esta pasta contém a collection do Postman utilizada para validar manualmente os endpoints da RAWG API antes da automação.

## 📂 Arquivos
- `rawg_api_collection.json`: Arquivo de exportação da Collection.

## 🚀 Como utilizar

1. Abra o Postman.
2. Clique em **Import** e selecione o arquivo `rawg_api_collection.json`.
3. Crie um Environment no Postman com as seguintes variáveis:
   - `base_url`: `https://api.rawg.io/api`
   - `api_key`: `SUA_CHAVE_DA_API`
4. Selecione o Environment e execute as requisições.

## ✅ Cenários Cobertos

### 1. Listar Jogos (GET /games)
- **Objetivo:** Validar o retorno da listagem de jogos padrão.
- **Validações Manuais:**
  - Status Code `200 OK`.
  - Presença da chave `count` (total de jogos).
  - Presença da lista `results`.
  - Tempo de resposta aceitável.

### 2. Validação de Erro de Chave (GET /games)
- **Objetivo:** Garantir que a API bloqueia requisições sem chave ou com chave inválida.
- **Parâmetros:** `key` inválida ou ausente.
- **Validações Manuais:**
  - Status Code `401 Unauthorized`.
  - Mensagem de erro: `{"error": "The key parameter is not provided"}` (ou mensagem similar de chave inválida).