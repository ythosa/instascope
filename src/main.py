import telegram

from src import config
from src.data import DataWork
from src.pic import Picture

# List of symbols
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


# url = "https://1001goroskop.ru/?znak="

# User Response Function
def generate_answer(text, chat_id, bot):
    text = text.rstrip()
    if len(text) > 0:
        if text == '/help':
            bot.send_message(chat_id=chat_id, text="Write <horoscope> to get horoscopes for all signs.\n"
                                                   "Write <horoscope some_sign> to get horoscope for this sign.\n"
                                                   "Write </signs> to get list of all signs.")
        elif text == '/signs':
            str_signs = ""
            for k, v in symbols.items():
                str_signs += "".join(str(k) + ' - ' + str(v) + '\n')
            bot.send_message(chat_id=chat_id, text=str_signs)
        else:
            text = text.split(' ')
            if text[0] == 'horoscope':
                if len(text) == 2:
                    if text[1] in symbols.values():
                        # return pic with this sign
                        sign = str(text[1])
                        name_of_pic = '_' + sign + '.png'
                        Picture.create(name_of_pic, sign)
                        bot.send_document(chat_id=chat_id, document=open(name_of_pic, 'rb'))
                    else:
                        # return wrong
                        bot.send_message(chat_id=chat_id, text="Invalid request")
                elif len(text) == 1:
                    # generate pic for all sings
                    for sign in symbols.values():
                        Picture.create(name='_' + str(sign) + '.png', z=sign)
                        bot.send_document(chat_id=chat_id, document=open('_' + str(sign) + '.png', 'rb'))
                else:
                    # return wrong
                    bot.send_message(chat_id=chat_id, text="Invalid request")
            else:
                # return wrong
                bot.send_message(chat_id=chat_id, text="Invalid request")
    else:
        # return wrong
        bot.send_message(chat_id=chat_id, text="Invalid request")


def main():
    # Create bot
    bot = telegram.Bot(token=config.TELEGRAM_TOKEN)
    last_upd = 0
    DataWork.init_data()
    while True:
        updates = bot.get_updates()
        new_upd = len(updates)
        chats_id = DataWork.get_chats_id()
        if new_upd != last_upd:  # Update Check. If the length has not changed, do nothing
            message_text = bot.get_updates()[-1].message.text  # Take text of message
            chat_id = bot.get_updates()[-1].message.chat_id  # Take chat ID
            if chat_id not in chats_id:  # If user first time have written to bot -> send "Hello Message"
                bot.send_message(chat_id=chat_id, text="Hello! I can generate horoscopes!\nWrite </help> to learn more")
                DataWork.push_to_chats_id(chat_id)
            else:
                generate_answer(message_text, chat_id, bot)  # User Response Function
        last_upd = new_upd


main()
