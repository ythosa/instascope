import re
from urllib.request import urlopen

from bs4 import BeautifulSoup

from src.config.config import CONFIG_FILE_PATH
from src.horoscope_generator.horoscope import Horoscope
from src.horoscope_generator.horoscope_list import HoroscopeList


class HoroscopeTextGenerator:
    def __init__(self, url):
        self._url = url
        horoscope_list = HoroscopeList()
        horoscope_list.configure_from_yml(CONFIG_FILE_PATH)
        self._symbols = horoscope_list

    def get_horoscope(self, sign) -> Horoscope:
        if not self._symbols.is_contains(sign):
            raise ValueError("passed symbol must be one of horoscope symbols")

        html_doc = urlopen(self._url + sign).read()
        soup = BeautifulSoup(html_doc, features="html.parser")
        soup = str(soup.find('p'))[3:-4]

        horoscope = "".join(re.split(r"([!?.]+)", soup, 3)[:4])

        sign = self._symbols.get_ru_translate_of_sign(sign)

        return Horoscope(str(sign).capitalize(), horoscope)
