import requests


class RawgClient:
    def __init__(self, base_url: str, api_key: str, timeout: int = 10):
        """
        Cliente responsável por realizar requisições à API RAWG.

        Args:
            base_url (str): URL base da API.
            api_key (str): Chave de autenticação.
            timeout (int): Tempo máximo de espera da requisição.
        """

        if not base_url or not api_key:
            raise ValueError("base_url e api_key são obrigatórios.")

        self.base_url = base_url.rstrip("/")  # Evita dupla barra no endpoint
        self.api_key = api_key
        self.timeout = timeout

    def get_games(self, page: int = 1, page_size: int = 10, **filters):
        """
        Busca lista de jogos na API RAWG.

        Args:
            page (int): Número da página.
            page_size (int): Quantidade de itens por página.
            **filters: Filtros opcionais suportados pela API (ex: search, platforms).

        Returns:
            requests.Response: Objeto de resposta da requisição.
        """

        endpoint = f"{self.base_url}/games"

        params = {
            "key": self.api_key,
            "page": page,
            "page_size": page_size,
        }

        params.update(filters)

        return requests.get(endpoint, params=params, timeout=self.timeout)