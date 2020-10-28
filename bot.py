import logging

from aiogram import Bot, Dispatcher, types, executor, filters

from config import config
from data import DataWorker
from horoscope_generator import HoroscopeGenerator
from models import HoroscopeList

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=config.TELEGRAM_TOKEN)
dp = Dispatcher(bot)

data_worker = DataWorker()  # Init data worker
horoscope_list = HoroscopeList()  # Init horoscope_list

# Init horoscope image creator
horoscope_image_creator = HoroscopeGenerator(horoscope_list, data_worker)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    :param message:
    :return:
    """
    await message.reply("Instascope is bot - generator of horoscopes!\n\n"
                        "You can:\n"
                        "\t\t- write /help to get some information;\n"
                        "\t\t- write /horoscope to get horoscope for any sign;\n"
                        "\t\t- write /horoscope_{some_sign} - to get horoscope for this sign;\n"
                        "\t\t- write /signs to get list of all signs.\n\n"
                        "Developer: Ythosa [ythosa.github.io]")


@dp.message_handler(commands=['signs'])
async def send_available_sings(message: types.Message):
    """
    This handler will be called when user sends `/sings` command
    :param message:
    :return:
    """

    await message.reply(str(horoscope_list))


@dp.message_handler(filters.RegexpCommandsFilter(regexp_commands=['horoscope_([a-z]+)']))
async def send_horoscope(message: types.Message, regexp_command):
    """
    This handler will be called when user sends `/horoscope {sign}` command
    :param message:
    :param regexp_command:
    :return:
    """
    sign = regexp_command.group(1)
    if not horoscope_list.is_contains(sign):
        await message.reply('Invalid sign')
        return

    picture_path = f"./instascope/.results/_{sign}.png"
    horoscope_image_creator.create(picture_path, sign)

    await message.reply_document(open(picture_path, 'rb'))


@dp.callback_query_handler(text='horoscope_taurus')
@dp.callback_query_handler(text='horoscope_aries')
@dp.callback_query_handler(text='horoscope_gemini')
@dp.callback_query_handler(text='horoscope_cancer')
@dp.callback_query_handler(text='horoscope_leo')
@dp.callback_query_handler(text='horoscope_libra')
@dp.callback_query_handler(text='horoscope_sagittarius')
@dp.callback_query_handler(text='horoscope_capricorn')
@dp.callback_query_handler(text='horoscope_aquarius')
@dp.callback_query_handler(text='horoscope_pisces')
@dp.callback_query_handler(text='horoscope_virgo')
@dp.callback_query_handler(text='horoscope_scorpio')
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    """
    This handler will be called when user presses some button from `/horoscope` command
    :param query:
    :return:
    """
    sign = query.data.split('_')[1]
    if not horoscope_list.is_contains(sign):
        await query.answer('Invalid sign')
        return

    picture_path = f"./.results/_{sign}.png"
    horoscope_image_creator.create(picture_path, sign)

    await bot.send_document(query.from_user.id, open(picture_path, 'rb'))


@dp.message_handler(commands='horoscope')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=3)

    text_and_data = [(s.emoji, f'horoscope_{s.en_translate}') for s in horoscope_list.get_horoscope_signs()]

    for i in range(0, len(text_and_data) // 4 + 1):
        row_btns = []
        for j in range(i * 3, i * 3 + 3):
            text, data = text_and_data[j]
            row_btns.append(types.InlineKeyboardButton(text, callback_data=data))
        keyboard_markup.row(*row_btns)

    await message.reply("Choose horoscope sign!", reply_markup=keyboard_markup)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
