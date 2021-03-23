import pytest
from clients.http_client import HttpClient


URL = 'https://rabota.by/search/vacancy'
KEYWORD = "python"
PYTHON_QUERY_PARAMS = {"area": "1002", "text": KEYWORD}
SHOTGUN_QUERY_PARAMS = {"area": "1002", "text": "shotgun"}
HEADER = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/39.0.2171.95 Safari/537.36'}


@pytest.fixture
def client():
    return HttpClient()


@pytest.fixture
def get_response_code(client):
    return client.get(URL, header=HEADER).status_code


@pytest.fixture
def search_result(client):
    return client.get(URL, params=SHOTGUN_QUERY_PARAMS, header=HEADER).text
