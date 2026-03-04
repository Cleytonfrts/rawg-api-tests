import pytest
from http import HTTPStatus
from api.client import RawgClient

# -----------------------------------------------------------------------------
# CENÁRIOS POSITIVOS
# -----------------------------------------------------------------------------

def test_get_games_status_code(client):
    """
    Objetivo: Validar se a API está online e autenticando corretamente.
    Técnica: Smoke Test.
    """
    # Act: Faz a requisição
    response = client.get_games()
    
    # Assert: Valida apenas o código de status
    assert response.status_code == HTTPStatus.OK


def test_get_games_contract(client):
    """
    Objetivo: Validar a estrutura dos dados (Contrato de API).
    Por que: O Front-end espera campos específicos (id, name, slug). 
             Se a API mudar isso, o sistema quebra.
    """
    # Act: Buscamos apenas 1 jogo para o teste ser rápido
    response = client.get_games(page_size=1)
    data = response.json()

    # Assert 1: Valida a "casca" do JSON (paginação)
    assert "count" in data, "O campo 'count' é obrigatório na resposta"
    assert "results" in data, "O campo 'results' é obrigatório na resposta"
    assert len(data["results"]) > 0, "A lista de jogos não deveria estar vazia"

    # Assert 2: Valida o conteúdo de um jogo (o primeiro da lista)
    first_game = data["results"][0]
    
    # Lista de campos que CONSIDERAMOS obrigatórios para o nosso negócio
    required_fields = ["id", "name", "slug", "released", "rating"]
    
    for field in required_fields:
        assert field in first_game, f"O campo '{field}' está faltando no jogo {first_game.get('name')}"


# -----------------------------------------------------------------------------
# CENÁRIOS NEGATIVOS
# -----------------------------------------------------------------------------

def test_get_games_unauthorized():
    """
    Objetivo: Garantir segurança. A API deve rejeitar chaves inválidas.
    """
    # Arrange: Criei um cliente propositalmente mal configurado.
    # Usei uma string fixa aqui apenas para garantir que é inválida.
    fake_client = RawgClient(base_url="https://api.rawg.io/api", api_key="INVALID_KEY_123")

    # Act: Tentamos buscar dados
    response = fake_client.get_games()

    # Assert: Deve ser barrado (401)
    assert response.status_code == HTTPStatus.UNAUTHORIZED