import re
from urllib.request import urlopen

from bs4 import BeautifulSoup

from src.config.config import CONFIG_FILE_PATH
from src.horoscope_generator.horoscope_list import HoroscopeList


class HoroscopeTextGenerator:
    def __init__(self, url):
        self._url = url
        self._symbols = HoroscopeList().configure_from_yml(CONFIG_FILE_PATH)

    def get_horoscope(self, symb):
        if symb not in self._symbols.keys():
            raise ValueError("passed symbol must be one of horoscope symbols")

        html_doc = urlopen(self._url + symb).read()
        soup = BeautifulSoup(html_doc, features="html.parser")
        soup = str(soup.find('p'))[3:-4]
        self._symbols[symb][1] = "".join(re.split(r"([!?.]+)", soup, 3)[:4])

        return self._symbols
