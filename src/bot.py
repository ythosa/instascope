import logging

from aiogram import Bot, Dispatcher, types, executor, filters

from src.config import config
from src.config.config import CONFIG_FILE_PATH
from src.horoscope_generator.horoscope_list import HoroscopeList
from src.horoscope_generator.pic import Picture

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
    horoscope_list = HoroscopeList()
    horoscope_list.configure_from_yml(CONFIG_FILE_PATH)
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
    horoscope_list = HoroscopeList()
    horoscope_list.configure_from_yml(CONFIG_FILE_PATH)
    if not horoscope_list.is_contains(sign):
        await message.reply('Invalid sign')
        return

    picture_path = f"./_results/_{sign}.png"
    Picture.create(picture_path, sign)

    await message.reply_document(open(picture_path, 'rb'))


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
