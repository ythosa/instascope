import datetime
import json

from src.config.config import DATA_FILE

# Work with JSON data file
class DataWork:
    data = {
        'updated_date': None,
        'chats_id': [],
        'horoscopes_text': {
            "taurus": None,
            "aries": None,
            "gemini": None,
            "cancer": None,
            "leo": None,
            "libra": None,
            "sagittarius": None,
            "capricorn": None,
            "aquarius": None,
            "pisces": None,
            "virgo": None,
            "scorpio": None,
        },
    }

    @staticmethod
    def init_data():
        with open(DATA_FILE, "w", encoding="utf-8") as data_file:
            json.dump(DataWork.data, data_file, indent=4)

    @staticmethod
    def get_chats_id():
        with open(DATA_FILE, "r", encoding="utf-8") as data_file:
            taken_data = dict(json.load(data_file))
        return taken_data['chats_id']

    @staticmethod
    def push_to_chats_id(chat_id):
        chats_id = DataWork.get_chats_id()
        chats_id.append(chat_id)
        with open(DATA_FILE, "r", encoding="utf-8") as data_file:
            taken_data = dict(json.load(data_file))
        taken_data['chats_id'] = chats_id
        with open(DATA_FILE, "w", encoding="utf-8") as data_file:
            json.dump(taken_data, data_file, indent=4)

    @staticmethod
    def get_symb_text(symb):
        with open(DATA_FILE, "r", encoding="utf-8") as data_file:
            taken_data = dict(json.load(data_file))
        return taken_data['horoscopes_text'][symb]

    @staticmethod
    def set_symb_text(symb, text):
        with open(DATA_FILE, "r", encoding="utf-8") as data_file:
            taken_data = dict(json.load(data_file))
        taken_data['horoscopes_text'][symb] = str(text)
        with open(DATA_FILE, "w", encoding="utf-8") as data_file:
            json.dump(taken_data, data_file, indent=4)

    @staticmethod
    def get_updated_date():
        with open(DATA_FILE, "r", encoding="utf-8") as data_file:
            taken_data = dict(json.load(data_file))
        return taken_data['updated_date']

    @staticmethod
    def set_updated_date(date):
        with open(DATA_FILE, "r", encoding="utf-8") as data_file:
            taken_data = dict(json.load(data_file))
        taken_data['updated_date'] = date
        with open("../../data_file.json", "w", encoding="utf-8") as data_file:
            json.dump(taken_data, data_file, indent=4)

    @staticmethod
    def get_now_date():
        # Get local date
        offset = datetime.timezone(datetime.timedelta(hours=3))
        date = datetime.datetime.now(offset)
        now_date = int(str(date)[8:11])
        return now_date
