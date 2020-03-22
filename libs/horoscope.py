# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib.request import urlopen


class Horoscope:
    @staticmethod
    def get_horoscope():
        # URL of horoscope site
        url = "https://1001goroskop.ru/?znak="
        # Horoscope symbols
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
        # Parse text
        for symb, text in symbols.items():
            html_doc = urlopen(url + symb).read()
            soup = BeautifulSoup(html_doc, features="html.parser")
            text[1] = str(soup.find('p'))[3:-4]
        return symbols
