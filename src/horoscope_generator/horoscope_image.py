import os
import re
from random import randint, choice
from textwrap import wrap
from urllib.request import urlopen

import requests
from PIL import Image, ImageDraw, ImageFont
from bs4 import BeautifulSoup
from saya import Vk

from src.config import config
from src.data.data import DataWorker
from src.horoscope_generator.horoscope import Horoscope
from src.horoscope_generator.horoscope_list import HoroscopeList

TITLE_FONT = ImageFont.truetype(config.FONT_PATH, 128)
FONT = ImageFont.truetype(config.FONT_PATH, 32 + 16)


class HoroscopeImageCreator:
    def __init__(self, horoscope_list: HoroscopeList, data_worker: DataWorker):
        self.horoscope_list = horoscope_list
        self._data_worker = data_worker
        self.public_pages = config.get_public_pages()

    def create(self, horoscope_picture_path: str = "pic.png", sign: str = "libra"):
        """
        Creates horoscope picture with title (sign) horoscope for this sign and meme
        :param horoscope_picture_path:
        :param sign:
        :return:
        """
        # Parse content
        (title, description) = self._get_horoscope(sign, config.HOROSCOPE_GENERATOR_URL)

        meme_path = 'meme.png'
        self._get_meme(meme_path)

        # params
        width, height = 1080, 1920
        meme_size = 900
        formatted_description = "\n".join(wrap(description, 41))
        start_height = 180

        back = Image.new("RGBA", (width, height), color="#282a36")
        meme = Image.open(meme_path).resize((meme_size, meme_size))
        draw = ImageDraw.Draw(back)

        # title
        w, h = draw.textsize(title, font=TITLE_FONT)
        draw.text(
            (width // 2 - w // 2, start_height),
            title, font=TITLE_FONT, fill="#f8f8f2")

        # description
        w1, h1 = draw.multiline_textsize(formatted_description, font=FONT)
        draw.multiline_text(
            (width // 2 - w1 // 2, start_height + h + (470 - h1) // 2),
            formatted_description, font=FONT, fill="#f8f8f2", align="center")
        back.paste(meme, (90, 930))

        back.save(horoscope_picture_path)
        if horoscope_picture_path != meme_path:
            os.remove(meme_path)

    def _get_meme(self, meme_path: str):
        """
        Gets random picture from random public page and writes it in the file.
        :param meme_path:
        :return:
        """
        choiced_public = choice(self.public_pages)
        vk = Vk(token=config.VK_TOKEN)
        photos = vk.photos.get(  # Gets all photos from album
            owner_id=choiced_public.owner_id, album_id=choiced_public.album_id,
            rev=randint(0, 1), offset=randint(0, 500), count=1000)
        photo = choice(photos["response"]["items"])  # Gets random photo from photos list.
        w = h = 0
        url = ""
        for size in photo["sizes"]:  # Gets max photo size.
            if size["width"] > w and size["height"] > h:
                w = size["width"]
                h = size["height"]
                url = size["url"]
        if url:
            # Write photo in file, if available.
            content = None
            while not content:
                try:
                    content = requests.get(url).content
                except requests.exceptions.ConnectionError:
                    continue
            with open(meme_path, "wb") as f:
                f.write(content)

    def _get_horoscope(self, sign: str, url: str) -> Horoscope:
        """
        Returns horoscope for passed sign
        :param sign:
        :param url:
        :return:
        """
        if not self.horoscope_list.is_contains(sign):
            raise ValueError("passed symbol must be one of horoscope symbols")

        sign = self.horoscope_list.get_en_translate_of_sign(sign)

        horoscope = self._data_worker.get_horoscope_for_sign(sign)
        if horoscope is not None:
            sign = self.horoscope_list.get_ru_translate_of_sign(sign)
            return Horoscope(str(sign).capitalize(), horoscope)

        html_doc = urlopen(url + sign).read()
        soup = BeautifulSoup(html_doc, features="html.parser")
        soup = str(soup.find('p'))[3:-4]

        horoscope = "".join(re.split(r"([!?.]+)", soup, 3)[:4])
        self._data_worker.update_sign_horoscope(sign, horoscope)
        sign = self.horoscope_list.get_ru_translate_of_sign(sign)

        return Horoscope(str(sign).capitalize(), horoscope)
