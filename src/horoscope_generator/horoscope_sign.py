from src.horoscope_generator.horoscope import Horoscope


class HoroscopeSign:
    horoscope: Horoscope

    def __init__(self, ru_translate, en_translate):
        self.ru_translate = ru_translate
        self.en_translate = en_translate

    def __str__(self):
        return f"{self.ru_translate} - {self.en_translate}"

    def __eq__(self, sign: str) -> bool:
        return self.ru_translate == sign or self.en_translate == sign
