# -*- coding: utf-8 -*-
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont

from .horoscope import Horoscope
from .meme import Meme


TITLE_FONT = ImageFont.truetype("data/DroidSans.ttf", 128)
FONT = ImageFont.truetype("data/DroidSans.ttf", 32 + 16)


class Picture:
    @staticmethod
    def create(name="pic.png", z="leo"):
        # --- Parse content --- #
        horoscope_list = Horoscope.get_horoscope()
        Meme.get()

        # --- Params --- #
        width, height = 1080, 1920
        memesize = int(width / 100 * 94)
        title = horoscope_list[z][0]
        desc = "\n".join(wrap(horoscope_list[z][1], 41))
        start_height = int(height / 100 * 1)

        back = Image.new("RGBA", (width, 1920), color="#282a36")
        meme = Image.open("meme.png").resize((memesize, memesize))
        draw = ImageDraw.Draw(back)

        # --- Title --- #
        w, h = draw.textsize(title, font=TITLE_FONT)
        draw.text(
            (width//2 - w//2, start_height),
            title, font=TITLE_FONT, fill="#f8f8f2")

        # --- Description --- #
        w1, h1 = draw.multiline_textsize(desc, font=FONT)
        draw.multiline_text(
            (width//2 - w1//2, start_height + h),
            desc, font=FONT, fill="#f8f8f2", align="center")

        back.paste(meme, (int(width / 100 * 3), height - memesize - start_height))
        back.save(name)
