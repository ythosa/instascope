from typing import List

from instascope.config import config
from instascope.models import HoroscopeSign


class HoroscopeList:
    _sign_list: List[HoroscopeSign] = []

    def __init__(self):
        self._sign_list = config.get_horoscope_signs()

    def __str__(self):
        return "\n".join([str(h) for h in self._sign_list])

    def is_contains(self, sign_name: str) -> bool:
        """
        Returns true is sign with name equals sign_name contains in self._sign_list
        :param sign_name: name of finding sign
        :return: is sign contains
        """
        for i in self._sign_list:
            if i.en_translate == sign_name or i.ru_translate == sign_name:
                return True

        return False

    def get_horoscope_signs(self) -> List[HoroscopeSign]:
        return self._sign_list

    def get_ru_translate_of_sign(self, sign_name: str) -> str:
        """
        Returns russian translate of passed sign_name
        :param sign_name:
        :return:
        """
        for s in self._sign_list:
            if sign_name == s:
                return s.ru_translate

    def get_en_translate_of_sign(self, sign_name: str) -> str:
        """
        Returns english translate of passed sign_name
        :param sign_name:
        :return:
        """
        for s in self._sign_list:
            if sign_name == s:
                return s.en_translate

    def _get_sign_index(self, sign_name: str) -> int:
        """
        Returns index of passed sign_name in _sign_list
        :param sign_name:
        :return:
        """
        index = 0
        for s in self._sign_list:
            if s == sign_name:
                break
            index += 1
        return index

    def get_ru_translate_signs(self) -> List[str]:
        """
        Returns all signs translated to russian
        :return:
        """
        return [s.ru_translate for s in self._sign_list]

    def get_en_translate_signs(self) -> List[str]:
        """
        Returns all signs translated to english
        :return:
        """
        return [s.en_translate for s in self._sign_list]
