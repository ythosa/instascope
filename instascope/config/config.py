from typing import List

import yaml

from instascope.models import HoroscopeSign, PublicPage

VK_TOKEN = "99a11d3599a11d3599a11d354099ce5222999a199a11d35c78d50e3779b82feb9455cee"
TELEGRAM_TOKEN = "1085045815:AAHYrjT04blrMpTlNke6wJCXqVqHbmkoReg"
HOROSCOPE_GENERATOR_URL = "https://1001goroskop.ru/?znak="
FONT_PATH = "/home/ythosa/Projects/instascope/fonts/DroidSans.ttf"
CONFIG_FILE_PATH = "/home/ythosa/Projects/instascope/instascope/config/config.yaml"


def _parse_yaml() -> dict:
    with open(CONFIG_FILE_PATH) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data


def get_horoscope_signs() -> List[HoroscopeSign]:
    horoscope_signs: List[HoroscopeSign] = []
    for ru, en in dict(CONFIG['signs']).items():
        horoscope_signs.append(HoroscopeSign(ru, en))

    return horoscope_signs


def get_public_pages() -> List[PublicPage]:
    public_pages: List[PublicPage] = []
    for name, bio in dict(CONFIG['public_pages']).items():
        public_pages.append(
            PublicPage(name=name, owner_id=int(bio['owner_id']), album_id=bio['album_id']))

    return public_pages


CONFIG = _parse_yaml()
