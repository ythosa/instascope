class HoroscopeSign:
    def __init__(self, ru_translate, en_translate, horoscope: str = ""):
        self.ru_translate = ru_translate
        self.en_translate = en_translate

    def __str__(self):
        return f"{self.ru_translate} - {self.en_translate}"
