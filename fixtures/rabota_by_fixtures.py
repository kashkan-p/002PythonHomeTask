import pytest
from clients.http_client import HttpClient
from models.rabota_by_parser import RabotaByParser


@pytest.fixture(scope='module')
def client():
    return HttpClient()


@pytest.fixture(scope='module')
def parser():
    return RabotaByParser()


@pytest.fixture
def rabota_by_response(client, parser):
    return client.get(parser.URL, params=parser.PYTHON_QUERY_PARAMS, header=parser.HEADER)
