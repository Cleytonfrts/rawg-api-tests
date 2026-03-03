from http import HTTPStatus

def test_get_games_status_code(client):
    """
    Valida se o endpoint /games retorna status 200 (OK)
    quando consultado com uma chave válida.
    """
    # Preparação é feita pela fixture 'client'

    response = client.get_games()

    # Assert (Validação)
    # Usamos HTTPStatus.OK para evitar "números mágicos" no código. 200 == OK.
    assert response.status_code == HTTPStatus.OK