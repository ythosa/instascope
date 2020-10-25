from typing import List

import yaml

from src.horoscope_generator.horoscope import Horoscope
from src.horoscope_generator.horoscope_sign import HoroscopeSign


class HoroscopeList:
    _sign_list: List[HoroscopeSign] = []

    def add_sign(self, sign: HoroscopeSign):
        self._sign_list.append(sign)

    def configure_from_yml(self, config_file_path: str):
        with open(config_file_path) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        for ru, en in data.items():
            self.add_sign(HoroscopeSign(ru, en))

    def __str__(self):
        return "\n".join([str(h) for h in self._sign_list])

    def is_contains(self, sign: str) -> bool:
        for i in self._sign_list:
            if i.en_translate == sign or i.ru_translate == sign:
                return True
        return False

    def get_ru_translate_of_sign(self, sign):
        for s in self._sign_list:
            if sign == s:
                return s.ru_translate

    def get_en_translate_of_sign(self, sign):
        for s in self._sign_list:
            if sign == s:
                return s.en_translate

    def _get_sign_index(self, sign: str):
        index = 0
        for s in self._sign_list:
            if s == sign:
                break
            index += 1
        return index

    def get_ru_translate_signs(self):
        return [s.ru_translate for s in self._sign_list]

    def get_en_translate_signs(self):
        return [s.en_translate for s in self._sign_list]

    def add_horoscope_for_sign(self, sign, text):
        index = self._get_sign_index(sign)
        horoscope_sign = self._sign_list[index]
        horoscope_sign.horoscope = Horoscope(title=horoscope_sign.ru_translate, description=text)
