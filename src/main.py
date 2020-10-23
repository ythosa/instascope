import logging

from aiogram import Bot, Dispatcher, types, executor, filters

from src import config
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

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=config.TELEGRAM_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    :param message:
    :return:
    """
    await message.reply("Write <horoscope> to get horoscopes for all signs.\n"
                        "Write <horoscope some_sign> to get horoscope for this sign.\n"
                        "Write </signs> to get list of all signs.")


@dp.message_handler(commands=['sings'])
async def send_available_sings(message: types.Message):
    """
    This handler will be called when user sends `/sings` command
    :param message:
    :return:
    """
    str_signs = ""
    for k, v in symbols.items():
        str_signs += "".join(str(k) + ' - ' + str(v) + '\n')
    await message.reply(str_signs)


@dp.message_handler(filters.RegexpCommandsFilter(regexp_commands=['horoscope_([a-z]+)']))
async def send_horoscope(message: types.Message, regexp_command):
    """
    This handler will be called when user sends `/horoscope {sign}` command
    :param message:
    :param regexp_command:
    :return:
    """
    sign = regexp_command.group(1)
    if sign not in symbols.values():
        await message.reply('Invalid sign')
        return

    name_of_pic = '_' + sign + '.png'
    Picture.create(name_of_pic, sign)

    await message.reply_document(open(name_of_pic, 'rb'))


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
