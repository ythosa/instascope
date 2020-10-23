from typing import List

from src.horoscope_generator.horoscope_sign import HoroscopeSign


class HoroscopeList:
    _sign_list: List[HoroscopeSign] = []

    def add_sign(self, sign: HoroscopeSign):
        self._sign_list.append(sign)

    def configure_from_yml(self, config_file_path: str):
        pass

    def __str__(self):
        return "\n".join([str(h) for h in self._sign_list])
