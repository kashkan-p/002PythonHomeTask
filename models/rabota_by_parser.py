"""This module describes RabotaByParser class which used for parsing rabota.by pages"""
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
        """This method takes html code of a search page and returns the range of pages of a search query
        :arg raw_html (html code of a page from http response)
        :return number of the last page in the query"""
        soup = BeautifulSoup(raw_html, "lxml")
        last_page = soup.find_all("span", class_="pager-item-not-in-short-range")[-1].find("a").text
        return int(last_page)

    @staticmethod
    def parse_vacancy_hrefs(raw_html):
        """This method takes html code of a search page and returns list of urls of every vacancy on a page
        :arg raw_html (html code of a page from http response)
        :return list of all vacancies links"""
        soup = BeautifulSoup(raw_html, "lxml")
        vacancies = soup.find_all("div", class_="vacancy-serp-item__row vacancy-serp-item__row_header")
        vacancy_list = []
        for item in vacancies:
            vacancy_list.append(item.find("a", class_="bloko-link").get("href"))
        return vacancy_list

    @staticmethod
    def parse_vacancy_description(raw_html):
        """This method takes html code of a vacancy page and returns string representation of vacancy title and
        description
        :arg raw_html (html code of a page from http response)
        :return description of a vacancy in string representation"""
        soup = BeautifulSoup(raw_html, "lxml")
        vacancy_desc = soup.find("div", class_="vacancy-section").prettify()
        return vacancy_desc

    @staticmethod
    def get_flat_list(list_of_lists):
        """This method merges list of sublists into a flat list
        :arg list_of_lists (list consisting of one level nested lists
        :return a flat list of all items in nrsted lists"""
        flat_list = []
        for sublist in list_of_lists:
            for item in sublist:
                flat_list.append(item)
        return flat_list

    @staticmethod
    def count_word_occurrences(data_list, str1, str2, str3):
        """This method counts occurrences of given word in every vacancy's description
        :arg data_list (a list containing all vacancies descriptions
        :arg str1, str2, str3 (substring to find in descriptions)
        :return a dictionary containing vacancy number and substring occurrences"""
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
    def count_average_word_occurrence(data_list, word):
        word_counted = 0
        for item in data_list:
            word_count = item.lower().count(word.lower())
            word_counted += word_count
        return {f"{word} average": word_counted}

