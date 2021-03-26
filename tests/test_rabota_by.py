"""This module contains tests for rabota.by pages executed with pytest library"""


def test_rabota_by_connection(rabota_by_python_response):
    assert rabota_by_python_response.status_code == 200, "The server response status code is not 200. " \
                                                         "The page is not available."


def test_results_for_python(rabota_by_python_response):
    assert "По запросу «python» ничего не найдено" not in rabota_by_python_response.text, "There should be results " \
                                                                                          "for «python» query "


def test_no_results_for_shotgun(rabota_by_shotgun_response):
    assert "По запросу «shotgun» ничего не найдено" in rabota_by_shotgun_response.text, "Shotgun should not be in " \
                                                                                        "search results "


def test_urls_list_length_equal_to_number_of_pages(parser, all_vacancies_list, rabota_by_python_response):
    last_page = parser.get_last_page_number(rabota_by_python_response.text)
    assert len(all_vacancies_list) == last_page, "Number of parsed pages is not equal to actual pages number"


def test_vacancies_number_on_first_page_equal_to_50(all_vacancies_list):
    assert len(all_vacancies_list[0]) == 50, "Number of vacancies displayed on the first page is not equal to 50"


def test_python_occurrence(rabota_by_python_response, avg_python_occurrence):
    python_count = rabota_by_python_response.text.lower().count("python")
    range_low = avg_python_occurrence["python average"] - 1
    range_high = avg_python_occurrence["python average"] + 1
    assert range_low <= python_count <= range_high, "The word count is out of bounds"


def test_flask_occurrence(rabota_by_python_response, avg_flask_occurrence):
    flask_count = rabota_by_python_response.text.lower().count("flask")
    range_low = avg_flask_occurrence["flask average"] - 1
    range_high = avg_flask_occurrence["flask average"] + 1
    assert range_low <= flask_count <= range_high, "The word count is out of bounds"


def test_linux_occurrence(rabota_by_python_response, avg_linux_occurrence):
    linux_count = rabota_by_python_response.text.lower().count("linux")
    range_low = avg_linux_occurrence["linux average"] - 1
    range_high = avg_linux_occurrence["linux average"] + 1
    assert range_low <= linux_count <= range_high, "The word count is out of bounds"
