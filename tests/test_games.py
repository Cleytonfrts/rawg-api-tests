import os
from http import HTTPStatus
from api.client import RawgClient

# =============================================================================
# GRUPO 1: CAMINHO FELIZ (SUCESSO)
# =============================================================================
class TestGamesSuccess:
    """Agrupa todos os cenários onde esperamos que a API responda corretamente."""

    def test_status_code_200(self, client):
        response = client.get_games()
        assert response.status_code == HTTPStatus.OK

    def test_contract_structure(self, client):
        response = client.get_games(page_size=1)
        data = response.json()

        assert "count" in data
        assert "results" in data
        assert len(data["results"]) > 0

        first_game = data["results"][0]
        required_fields = ["id", "name", "slug", "released", "rating"]
        
        for field in required_fields:
            assert field in first_game, f"Campo '{field}' faltando no JSON."


# =============================================================================
# GRUPO 2: CAMINHO TRISTE (ERROS E SEGURANÇA)
# =============================================================================
class TestGamesErrors:
    """Agrupa todos os cenários onde simulamos ataques ou erros do usuário."""

    def test_unauthorized_401(self):

        base_url = os.getenv("BASE_URL")
        
        # Cliente com chave falsa proposital
        fake_client = RawgClient(base_url=base_url, api_key="CHAVE_INVALIDA_123")

        response = fake_client.get_games()
        assert response.status_code == HTTPStatus.UNAUTHORIZED