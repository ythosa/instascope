import os
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont

from src.config import config
from src.horoscope_generator.horoscope_text_generator import HoroscopeTextGenerator
from src.horoscope_generator.meme import Meme

TITLE_FONT = ImageFont.truetype(config.FONT_PATH, 128)
FONT = ImageFont.truetype(config.FONT_PATH, 32 + 16)


class Picture:
    @staticmethod
    def create(name="pic.png", z="libra"):
        # Parse content
        horoscope_text_generator = HoroscopeTextGenerator(config.HOROSCOPE_GENERATOR)

        (title, description) = horoscope_text_generator.get_horoscope(z)

        Meme.get()

        # params
        width, height = 1080, 1920
        meme_size = 900
        formatted_description = "\n".join(wrap(description, 41))
        start_height = 180

        back = Image.new("RGBA", (width, height), color="#282a36")
        meme = Image.open("meme.png").resize((meme_size, meme_size))
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
        back.save(name)
        if name != "meme.png":
            os.remove("meme.png")
