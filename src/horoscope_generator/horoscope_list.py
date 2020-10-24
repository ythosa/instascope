from typing import List

import yaml

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
