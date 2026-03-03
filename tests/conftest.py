import os
import pytest
from dotenv import load_dotenv
from api.client import RawgClient

# Carrega as variáveis de ambiente uma vez antes dos testes
load_dotenv()

@pytest.fixture
def client():
    """
    Fixture que instancia o cliente da API.
    Ela garante que todo teste receba um cliente pronto e configurado.
    """
    base_url = os.getenv("BASE_URL")
    api_key = os.getenv("RAWG_API_KEY")
    
    # Fail Fast: Se não configurar o .env, os testes nem começam
    if not base_url or not api_key:
        pytest.fail("Variáveis BASE_URL e RAWG_API_KEY não definidas no .env")
        
    return RawgClient(base_url=base_url, api_key=api_key)