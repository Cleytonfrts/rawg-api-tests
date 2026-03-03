import pytest
from http import HTTPStatus

def test_get_games_status_code(client):
    """
    Valida se o endpoint de jogos retorna status 200 (OK).
    """
    response = client.get_games()
    
    # Assert (Validação)
    # Usamos HTTPStatus.OK para ficar mais legível que apenas "200"
    assert response.status_code == HTTPStatus.OK