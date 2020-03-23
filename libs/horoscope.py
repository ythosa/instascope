# -*- coding: utf-8 -*-

import re
from bs4 import BeautifulSoup
from urllib.request import urlopen


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
        # Parse text
        html_doc = urlopen(Horoscope.url + symb).read()
        soup = BeautifulSoup(html_doc, features="html.parser")
        soup = str(soup.find('p'))[3:-4]
        Horoscope.symbols[symb][1] = "".join(re.split(r"([\!\?\.]+)", soup, 3)[:4])
        return Horoscope.symbols
