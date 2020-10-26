import logging

from aiogram import Bot, Dispatcher, types, executor, filters

from instascope.config import config
from instascope.data import DataWorker
from instascope.horoscope_generator import HoroscopeGenerator
from instascope.models import HoroscopeList

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
    await message.reply("Write </help> to get some information.\n"
                        "Write </horoscope_{some_sign}> to get horoscope for this sign.\n"
                        "Write </signs> to get list of all signs.")


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

    picture_path = f"./instascope/_results/_{sign}.png"
    horoscope_image_creator.create(picture_path, sign)

    await message.reply_document(open(picture_path, 'rb'))


# Use multiple registrators. Handler will execute when one of the filters is OK
@dp.callback_query_handler(text='no')  # if cb.data == 'no'
@dp.callback_query_handler(text='yes')  # if cb.data == 'yes'
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    answer_data = query.data
    # always answer callback queries, even if you have nothing to say
    await query.answer(f'You answered with {answer_data!r}')

    if answer_data == 'yes':
        text = 'Great, me too!'
    elif answer_data == 'no':
        text = 'Oh no...Why so?'
    else:
        text = f'Unexpected callback data {answer_data!r}!'

    await bot.send_message(query.from_user.id, text)


@dp.message_handler(commands='horoscope')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=3)
    # default row_width is 3, so here we can omit it actually
    # kept for clearness

    horoscope_emoji = {
        'taurus': '♉',
        'aries': '♈',
        'gemini': '♊',
        'cancer': '♋',
        'leo': '♌',
        'libra': '♎',
        'sagittarius': '♐',
        'capricorn': '♑',
        'aquarius': '♒',
        'pisces': '♓',
        'virgo': '♍',
        'scorpio': '♏',
    }

    text_and_data = [(s.emoji, f'horoscope_{s.en_translate}') for s in horoscope_list.get_horoscope_signs()]

    for i in range(0, len(text_and_data) // 4 + 1):
        row_btns = []
        for j in range(i, i+3):
            text, data = text_and_data[j]
            row_btns.append(types.InlineKeyboardButton(text, callback_data=data))
        keyboard_markup.row(*row_btns)

    await message.reply("Choose horoscope sign!", reply_markup=keyboard_markup)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
