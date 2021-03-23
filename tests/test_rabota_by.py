def test_rabota_by_connection(rabota_by_response):
    assert rabota_by_response.status_code == 200, "The server does not respond"


def test_no_results_for_shotgun(rabota_by_response):
    assert "shotgun" not in rabota_by_response.text, "Shotgun should not be in search results"


def test_python_occurrence(rabota_by_response, avg_word_occurrence):
    python_count = rabota_by_response.text.lower().count("python")
    range_low = avg_word_occurrence["python average occurrence"] - 1
    range_high = avg_word_occurrence["python average occurrence"] + 1
    assert range_low <= python_count <= range_high, "The word count is out of bounds"


def test_flask_occurrence(rabota_by_response, avg_word_occurrence):
    flask_count = rabota_by_response.text.lower().count("flask")
    range_low = avg_word_occurrence["flask average occurrence"] - 1
    range_high = avg_word_occurrence["flask average occurrence"] + 1
    assert range_low <= flask_count <= range_high, "The word count is out of bounds"


def test_linux_occurrence(rabota_by_response, avg_word_occurrence):
    linux_count = rabota_by_response.text.lower().count("linux")
    range_low = avg_word_occurrence["linux average occurrence"] - 1
    range_high = avg_word_occurrence["linux average occurrence"] + 1
    assert range_low <= linux_count <= range_high, "The word count is out of bounds"
