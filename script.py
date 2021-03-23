from models.rabota_by_parser import RabotaByParser
from clients.http_client import HttpClient


URL = 'https://rabota.by/search/vacancy'
KEYWORD = "python"
PARAMS = {"area": "1002", "text": KEYWORD}
HEADER = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/39.0.2171.95 Safari/537.36'}

if __name__ == '__main__':
    # Initializing client and parser objects
    client = HttpClient()
    parser = RabotaByParser()

    # Getting the first search page html code
    start_page = client.get(URL, params=PARAMS, header=HEADER).text
    # Getting numbers of pages of a search query
    last_page = parser.get_last_page_number(start_page)

    # Getting the list of vacancy urls on an every search page
    vacancy_urls = []
    for number in range(parser.FIRST_PAGE_NUMBER, last_page):
        PARAMS["page"] = number
        page = client.get(URL, params=PARAMS, header=HEADER).text
        vacancy_urls.append(parser.parse_vacancy_hrefs(page))

    # Merging all urls to one flat list
    all_vacancies_urls = parser.get_flat_list(vacancy_urls)

    # Getting html code of every vacancy page and adding it to a list
    vacancy_description_raw = []
    for vacancy_url in all_vacancies_urls:
        vacancy_description_raw.append(client.get(vacancy_url, header=HEADER).text)

    # Parsing vacancy title and description and adding it to a list
    vacancies_parsed = []
    for vacancy in vacancy_description_raw:
        parsed = parser.parse_vacancy_description(vacancy)
        vacancies_parsed.append(parsed)

    # Counting occurrences of the given words in each vacancy description
    counted = parser.count_word_occurrences(vacancies_parsed, "python", "linux", "flask")
    # Counting average occurrences of the given words
    avg_occurrence = parser.count_average_word_occurrence(vacancies_parsed, "python", "linux", "flask")
