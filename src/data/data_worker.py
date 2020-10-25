import json
from datetime import datetime
from typing import Optional

import redis


class DataWorker:
    def __init__(self):
        self._db = redis.Redis()

    def update_sign_horoscope(self, sign, horoscope):
        self._db.set(sign, json.dumps({
            'horoscope': horoscope,
            'update_day': datetime.now().day
        }))

    def get_horoscope_for_sign(self, sign) -> Optional[str]:
        v = self._db.get(sign)
        if v is None:
            return None

        v = bytearray(v).decode("utf-8")
        v = dict(json.loads(v))
        if v['update_day'] != datetime.now().day:
            return None

        return v['horoscope']
