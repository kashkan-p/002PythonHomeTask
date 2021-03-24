import pytest
from clients.http_client import HttpClient
from models.rabota_by_parser import RabotaByParser


@pytest.fixture(scope='module')
def client():
    return HttpClient()


@pytest.fixture(scope='module')
def parser():
    return RabotaByParser()


@pytest.fixture(scope='module')
def rabota_by_python_response(client, parser):
    return client.get(parser.URL, params=parser.PYTHON_QUERY_PARAMS, header=parser.HEADER)


@pytest.fixture
def rabota_by_shotgun_response(client, parser):
    return client.get(parser.URL, params=parser.SHOTGUN_QUERY_PARAMS, header=parser.HEADER)


@pytest.fixture(scope='module')
def avg_word_occurrence(client, parser, rabota_by_response):
    last_page = parser.get_last_page_number(rabota_by_response.text)

    vacancy_urls = []
    for number in range(parser.FIRST_PAGE_NUMBER, last_page):
        parser.PYTHON_QUERY_PARAMS["page"] = number
        page = client.get(parser.URL, params=parser.PYTHON_QUERY_PARAMS, header=parser.HEADER).text
        vacancy_urls.append(parser.parse_vacancy_hrefs(page))

    all_vacancies_urls = parser.get_flat_list(vacancy_urls)

    vacancy_description_raw = []
    for vacancy_url in all_vacancies_urls:
        vacancy_description_raw.append(client.get(vacancy_url, header=parser.HEADER).text)

    vacancies_parsed = []
    for vacancy in vacancy_description_raw:
        parsed = parser.parse_vacancy_description(vacancy)
        vacancies_parsed.append(parsed)

    avg_occurrence = parser.count_average_word_occurrence(vacancies_parsed, "python", "linux", "flask")

    return avg_occurrence
