from bs4 import BeautifulSoup


class RabotaByParser:
    """RabotaByParser provides parsing of particular data from raw html code of rabota.by pages"""

    URL = 'https://rabota.by/search/vacancy'
    PYTHON_QUERY_PARAMS = {"area": "1002", "text": "python"}
    SHOTGUN_QUERY_PARAMS = {"area": "1002", "text": "shotgun"}
    HEADER = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/39.0.2171.95 Safari/537.36'}
    FIRST_PAGE_NUMBER = 0

    @staticmethod
    def get_last_page_number(raw_html):
        """This method takes html code of a search page and returns the range of pages of a search query"""
        soup = BeautifulSoup(raw_html, "lxml")
        last_page = soup.find_all("span", class_="pager-item-not-in-short-range")[-1].find("a").text
        return int(last_page)

    @staticmethod
    def parse_vacancy_hrefs(raw_html):
        """This method takes html code of a search page and returns list of urls of every vacancy on a page"""
        soup = BeautifulSoup(raw_html, "lxml")
        vacancies = soup.find_all("div", class_="vacancy-serp-item__row vacancy-serp-item__row_header")
        vacancy_list = []
        for item in vacancies:
            vacancy_list.append(item.find("a", class_="bloko-link").get("href"))
        return vacancy_list

    @staticmethod
    def parse_vacancy_description(raw_html):
        """This method takes html code of a vacancy page and returns string representation of vacancy title and
        description """
        soup = BeautifulSoup(raw_html, "lxml")
        vacancy_desc = soup.find("div", class_="vacancy-section").prettify()
        return vacancy_desc

    @staticmethod
    def get_flat_list(list_of_lists):
        """This method merges list of sublists into a flat list"""
        flat_list = []
        for sublist in list_of_lists:
            for item in sublist:
                flat_list.append(item)
        return flat_list

    @staticmethod
    def count_word_occurrences(data_list, str1, str2, str3):
        """This method counts occurrences of given word in every vacancy's description"""
        counted = {}
        vacancy_num = 1
        for item in data_list:
            str1_count = item.lower().count(str1.lower())
            str2_count = item.lower().count(str2.lower())
            str3_count = item.lower().count(str3.lower())
            counted[f"Vacancy №{vacancy_num}"] = {f"{str1}": str1_count, f"{str2}": str2_count, f"{str3}": str3_count}
            vacancy_num += 1
        return counted

    @staticmethod
    def count_average_word_occurrence(data_list, str1, str2, str3):
        """This method counts average occurrences count of given word in a whole search query"""
        str1_counted = 0
        str2_counted = 0
        str3_counted = 0
        for item in data_list:
            str1_count = item.lower().count(str1.lower())
            str2_count = item.lower().count(str2.lower())
            str3_count = item.lower().count(str3.lower())
            str1_counted += str1_count
            str2_counted += str2_count
            str3_counted += str3_count
        return {f"{str1} average occurrence": str1_counted / len(data_list),
                f"{str2} average occurrence": str2_counted / len(data_list),
                f"{str3} average occurrence": str3_counted / len(data_list)}

    # @staticmethod
    # def get_failed_search_message(raw_html):
    #     soup = BeautifulSoup(raw_html, "lxml")
    #     msg = soup.find("div", id="HH-React-Root").find("h1", class_="bloko-header-1").text
    #     return msg
