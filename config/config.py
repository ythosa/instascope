from typing import List

import os
import yaml

from models import HoroscopeSign, PublicPage

VK_TOKEN = os.getenv("VK_TOKEN")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
HOROSCOPE_GENERATOR_URL = "https://1001goroskop.ru/?znak="
FONT_PATH = "./fonts/DroidSans.ttf"
CONFIG_FILE_PATH = "./config/config.yaml"


def _parse_yaml() -> dict:
    with open(CONFIG_FILE_PATH) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data


def get_horoscope_signs() -> List[HoroscopeSign]:
    horoscope_signs: List[HoroscopeSign] = []
    for ru, bio in dict(CONFIG['signs']).items():
        bio = dict(bio)
        en = bio['named']
        emoji = bio['emoji']
        horoscope_signs.append(HoroscopeSign(ru, en, emoji))

    return horoscope_signs


def get_public_pages() -> List[PublicPage]:
    public_pages: List[PublicPage] = []
    for name, bio in dict(CONFIG['public_pages']).items():
        public_pages.append(
            PublicPage(name=name, owner_id=int(bio['owner_id']), album_id=bio['album_id']))

    return public_pages


CONFIG = _parse_yaml()
