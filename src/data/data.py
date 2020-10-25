from typing import Optional

import redis


class DataWorker:
    def __init__(self):
        self._db = redis.Redis()

    def update_sign_horoscope(self, sign, horoscope):
        self._db.set(sign, horoscope)

    def get_horoscope_for_sign(self, sign) -> Optional[str]:
        v = self._db.get(sign)
        if v is not None:
            return v.decode("utf-8")

        return None
