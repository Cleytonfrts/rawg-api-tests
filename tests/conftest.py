import os
import pytest
from dotenv import load_dotenv
from api.client import RawgClient

@pytest.fixture
def client():
    """
    Fixture que prepara e retorna uma instância do RawgClient.
    Ela é executada antes de cada teste que pedir o argumento 'client'.
    """
    # 1. Carrega variáveis de ambiente
    load_dotenv()

    base_url = os.getenv("BASE_URL")
    api_key = os.getenv("RAWG_API_KEY")

    # 2. Se a config estiver errada, para tudo agora.
    if not base_url or not api_key:
        pytest.fail("ERRO CRÍTICO: As variáveis BASE_URL e RAWG_API_KEY não foram encontradas no .env")

    # 3. Retorna o cliente pronto para uso
    return RawgClient(base_url=base_url, api_key=api_key)