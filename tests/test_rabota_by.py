def test_rabota_by_connection(rabota_by_python_response):
    assert rabota_by_python_response.status_code == 200, "The server does not respond"


def test_results_for_python(rabota_by_python_response):
    assert "По запросу «python» ничего не найдено" not in rabota_by_python_response.text, "There should be results " \
                                                                                          "for «python» query "


def test_no_results_for_shotgun(rabota_by_shotgun_response):
    assert "По запросу «shotgun» ничего не найдено" in rabota_by_shotgun_response.text, "Shotgun should not be in " \
                                                                                        "search results "


def test_urls_list_length_equal_to_number_of_pages(last_page, all_vacancies_list):
    assert len(all_vacancies_list) == last_page, "Number of parsed pages is not equal to actual pages number"


def test_vacancies_number_on_first_page_equal_to_50(all_vacancies_list):
    assert len(all_vacancies_list[0]) == 50, "Number of vacancies displayed on the first page is not equal to 50"


def test_python_occurrence(rabota_by_python_response, avg_word_occurrence):
    python_count = rabota_by_python_response.text.lower().count("python")
    range_low = avg_word_occurrence["python average occurrence"] - 1
    range_high = avg_word_occurrence["python average occurrence"] + 1
    assert range_low <= python_count <= range_high, "The word count is out of bounds"


def test_flask_occurrence(rabota_by_python_response, avg_word_occurrence):
    flask_count = rabota_by_python_response.text.lower().count("flask")
    range_low = avg_word_occurrence["flask average occurrence"] - 1
    range_high = avg_word_occurrence["flask average occurrence"] + 1
    assert range_low <= flask_count <= range_high, "The word count is out of bounds"


def test_linux_occurrence(rabota_by_python_response, avg_word_occurrence):
    linux_count = rabota_by_python_response.text.lower().count("linux")
    range_low = avg_word_occurrence["linux average occurrence"] - 1
    range_high = avg_word_occurrence["linux average occurrence"] + 1
    assert range_low <= linux_count <= range_high, "The word count is out of bounds"
