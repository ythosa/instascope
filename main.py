# -*- coding: utf-8 -*-
import asyncio
import re

from saya import AVk, AUploader

from libs.pic import Picture
from libs.horoscope import Horoscope


class MyAVk(AVk):
    symbols = {
        "телец": "taurus",
        "овен": "aries",
        "близнецы": "gemini",
        "рак": "cancer",
        "лев": "leo",
        "весы": "libra",
        "стрелец": "sagittarius",
        "козерог": "capricorn",
        "водолей": "aquarius",
        "рыбы": "pisces",
        "дева": "virgo",
        "скорпион": "scorpio",
    }
    async def message_new(self, event):
        # --- variables --- #
        self.event = event["object"]["message"]
        self.text = self.event["text"]
        self.peer_id = self.event["peer_id"]
        self.from_id = self.event["from_id"]

        if re.match(self.horoscope_pattern, self.text, re.IGNORECASE):
            matched = re.findall(self.horoscope_pattern, self.text, re.IGNORECASE)[0].lower()
            print(matched)
            # --- create picture --- #
            name = "pic_for_%d_%d.png" % (self.peer_id, self.from_id)
            Picture.create(Horoscope.symbols, name, MyAVk.symbols[matched])

            # --- upload image --- #
            photo = await self.uploader.message_photo(name, self.peer_id)
            print(photo)
            photo = AUploader.format(photo)
            print(photo)

            # --- send message --- #
            await self.messages.send(
                attachment=photo, random_id=0,
                peer_id=self.peer_id)

    async def main(self):
        self.pattern = "|".join(MyAVk.symbols.keys())
        self.horoscope_pattern = r"\A\s*гороскоп\s*(" + self.pattern + r")\s*\Z"
        print("launched")
        await self.start_listen()


if __name__ == '__main__':
    vk = MyAVk(
        token="",
        group_id=123123123)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(vk.main())
