import pytest
from clients.http_client import HttpClient

HEADER = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/39.0.2171.95 Safari/537.36'}


@pytest.fixture
def client():
    return HttpClient()


@pytest.fixture
def get_response_code(client):
    return client.get("https://rabota.by/search/vacancy?text=python", header=HEADER).status_code


@pytest.fixture
def search_result(client):
    return client.get("https://rabota.by/search/vacancy?area=1002&text=shotgun", header=HEADER).text
