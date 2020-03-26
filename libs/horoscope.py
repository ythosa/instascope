# -*- coding: utf-8 -*-

import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from data import DataWork


class Horoscope:
    # URL of horoscope site
    url = "https://1001goroskop.ru/?znak="
    symbols = {
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

    @staticmethod
    def get_horoscope(symb="leo"):
        if DataWork.get_now_date() == DataWork.get_updated_date():
            # Take from data file
            return DataWork.get_symb_text(symb)
        else:
            # Generate new and write to data file
            # Parse text
            html_doc = urlopen(Horoscope.url + symb).read()
            soup = BeautifulSoup(html_doc, features="html.parser")
            soup = str(soup.find('p'))[3:-4]
            Horoscope.symbols[symb][1] = "".join(re.split(r"([\!\?\.]+)", soup, 3)[:4])
            DataWork.set_symb_text(symb, Horoscope.symbols[symb][1])
            return Horoscope.symbols
