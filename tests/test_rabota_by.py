from fixtures.rabota_by_fixtures import *


def test_response(get_response_code):
    assert get_response_code == 200


def test_search(search_result):
    assert "По запросу «shotgun» ничего не найдено" in search_result
