import pytest
from clients.http_client import HttpClient
from models.rabota_by_parser import RabotaByParser


@pytest.fixture(scope='module')
def client():
    """This fixture returns a client for http requests
    :return an HttpClient class object"""
    return HttpClient()


@pytest.fixture(scope='module')
def parser():
    """This fixture returns a parser for rabota.by pages
    :return an RabotaByParser class object"""
    return RabotaByParser()


@pytest.fixture(scope='module')
def rabota_by_python_response(client, parser):
    """This fixture gets response from rabota.by with "python" search query
    :arg client (instance of HttpClient)
    :arg parser (instance of RabotaByParser)
    :return http response object"""
    return client.get(parser.URL, params=parser.PYTHON_QUERY_PARAMS, header=parser.HEADER)


@pytest.fixture
def rabota_by_shotgun_response(client, parser):
    """This fixture gets response from rabota.by with "shotgun" search query
    :arg client (instance of HttpClient)
    :arg parser (instance of RabotaByParser)
    :return http response object"""
    return client.get(parser.URL, params=parser.SHOTGUN_QUERY_PARAMS, header=parser.HEADER)


@pytest.fixture(scope='module')
def last_page(client, parser, rabota_by_python_response):
    """This fixture finds the number of the last page in a search query
    :arg client (instance of HttpClient)
    :arg parser (instance of RabotaByParser)
    :arg rabota_by_python_response (http response object
    :return int number of the last page"""
    return parser.get_last_page_number(rabota_by_python_response.text)


@pytest.fixture(scope='module')
def all_vacancies_list(client, parser, rabota_by_python_response, last_page):
    """This fixture gets oll vacancies links from the first to the las page
    :arg client (instance of HttpClient)
    :arg parser (instance of RabotaByParser)
    :arg rabota_by_python_response (http response object)
    :arg last_page (number of the last page)
    :return list of all vacancies"""
    vacancy_urls = []
    for number in range(parser.FIRST_PAGE_NUMBER, last_page):
        parser.PYTHON_QUERY_PARAMS["page"] = number
        page = client.get(parser.URL, params=parser.PYTHON_QUERY_PARAMS, header=parser.HEADER).text
        vacancy_urls.append(parser.parse_vacancy_hrefs(page))
    return vacancy_urls


@pytest.fixture(scope='module')
def avg_word_occurrence(client, parser, all_vacancies_list):
    """This fixture counts average occurrences of words in vacancy tescriptions
    :arg client (instance of HttpClient)
    :arg parser (instance of RabotaByParser)
    :arg all_vacancies_list (ist of all vacancies)
    :return dict with a number of average occurrences of words"""

    all_vacancies_urls = parser.get_flat_list(all_vacancies_list)

    vacancy_description_raw = []
    for vacancy_url in all_vacancies_urls:
        vacancy_description_raw.append(client.get(vacancy_url, header=parser.HEADER).text)

    vacancies_parsed = []
    for vacancy in vacancy_description_raw:
        parsed = parser.parse_vacancy_description(vacancy)
        vacancies_parsed.append(parsed)

    avg_occurrence = parser.count_average_word_occurrence(vacancies_parsed, "python", "linux", "flask")

    return avg_occurrence
