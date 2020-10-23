import re
from urllib.request import urlopen

from bs4 import BeautifulSoup

from src.data import DataWork


class HoroscopeTextGenerator:
    _symbols = {
        "taurus": ["Телец", ""],
        "aries": ["Овен", ""],
        "gemini": ["Близнецы", ""],
        "cancer": ["Рак", ""],
        "leo": ["Лев", ""],
        "libra": ["Весы", ""],
        "sagittarius": ["Стрелец", ""],
        "capricorn": ["Козерог", ""],
        "aquarius": ["Водолей", ""],
        "pisces": ["Рыбы", ""],
        "virgo": ["Дева", ""],
        "scorpio": ["Скорпион", ""],
    }

    def __init__(self, url):
        self._url = url

    def get_horoscope(self, symb):
        if symb not in self._symbols.keys():
            raise ValueError("passed symbol must be one of horoscope symbols")

        if (DataWork.get_now_date() == DataWork.get_updated_date()) and (DataWork.get_symb_text(symb) is not None):
            # Take from data file
            self._symbols[symb][1] = DataWork.get_symb_text(symb)
            return self._symbols
        else:
            # Generate new and write to data file
            # Parse text
            html_doc = urlopen(self._url + symb).read()
            soup = BeautifulSoup(html_doc, features="html.parser")
            soup = str(soup.find('p'))[3:-4]
            self._symbols[symb][1] = "".join(re.split(r"([!?.]+)", soup, 3)[:4])

            DataWork.set_symb_text(symb, self._symbols[symb][1])
            DataWork.set_updated_date(DataWork.get_now_date())

            return self._symbols
