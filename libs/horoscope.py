# -*- coding: utf-8 -*-

import re
from bs4 import BeautifulSoup
from urllib.request import urlopen


class Horoscope:
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

    @classmethod
    def get_horoscope(cls, symb="leo"):
        # URL of horoscope site
        url = "https://1001goroskop.ru/?znak="
        # Horoscope symbols
        
        # Parse text
        html_doc = urlopen(url + symb).read()
        soup = BeautifulSoup(html_doc, features="html.parser")
        soup = str(soup.find('p'))[3:-4]
        cls.symbols[symb][1] = "".join(re.split(r"([\!\?\.]+)", soup, 3)[:4])
        return cls.symbols
