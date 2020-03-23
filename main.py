# -*- coding: utf-8 -*-
import asyncio
import re

# from saya import AVk, AUploader
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InputMediaPhoto

from libs.pic import Picture
from libs.horoscope import Horoscope

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


def generate_horoscope(text):
    text = text.rstrip().split(' ')
    if text[0] == 'horoscope':
        if len(text) == 2:
            if text[1] in symbols.values():
                # return pic with this sign
                pass
            else:
                # return wrong
                pass
        elif len(text) == 1:
            # generate pic for all sings
            pass
        else:
            # return wrong
            pass
    else:
        # return wrong
        pass


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hello, I can generate horoscopes!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Write "horoscope" to have horoscope for all signs.\n'
                              'Write: "horoscope <some_sign>" to get horoscope for this sign.\n'
                              'Horoscope signs: ["taurus", "aries", "gemini", "cancer",'
                              '"leo", "libra", "sagittarius", "capricorn","aquarius","pisces","virgo","scorpio"].')


def generate(update, context):
    """Echo the user message."""
    update.message.reply_text(generate_horoscope(update.message.text))
    from io import BytesIO
    bio = BytesIO()
    bio.name = 'image.jpeg'
    image.save(bio, 'JPEG')
    bio.seek(0)
    bot.send_photo(chat_id, photo=bio)


def main():
    """Start bot"""
    updater = Updater("1085045815:AAESWK5yzQTTsjDWBzkvYwdrkVK9rUgLAoQ", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, generate))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()


# # # # # # # # # # # # # # #

# class MyAVk(AVk):

#     async def message_new(self, event):
#         # --- variables --- #
#         self.event = event["object"]["message"]
#         self.text = self.event["text"]
#         self.peer_id = self.event["peer_id"]
#         self.from_id = self.event["from_id"]
#
#         if re.match(self.horoscope_pattern, self.text, re.IGNORECASE):
#             matched = re.findall(self.horoscope_pattern, self.text, re.IGNORECASE)[0].lower()
#             print(matched)
#             # --- create picture --- #
#             name = "pic_for_%d_%d.png" % (self.peer_id, self.from_id)
#             Picture.create(Horoscope.symbols, name, MyAVk.symbols[matched])
#
#             # --- upload image --- #
#             photo = await self.uploader.message_photo(name, self.peer_id)
#             print(photo)
#             photo = AUploader.format(photo)
#             print(photo)
#
#             # --- send message --- #
#             await self.messages.send(
#                 attachment=photo, random_id=0,
#                 peer_id=self.peer_id)
#
#     async def main(self):
#         self.pattern = "|".join(MyAVk.symbols.keys())
#         self.horoscope_pattern = r"\A\s*гороскоп\s*(" + self.pattern + r")\s*\Z"
#         print("launched")
#         await self.start_listen()
#
#
# if __name__ == '__main__':
#     vk = MyAVk(
#         token="",
#         group_id=123123123)
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(vk.main())
