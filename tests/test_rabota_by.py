def test_rabota_by_connection(rabota_by_response):
    assert rabota_by_response.status_code == 200


def test_no_results_for_shotgun(rabota_by_response):
    assert "shotgun" not in rabota_by_response.text
