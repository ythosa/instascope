# -*- coding: utf-8 -*-
from libs.pic import Picture
from libs.horoscope import Horoscope

signs = Horoscope.get_horoscope()

# Generate pictures for each sign
for sign in signs.keys():
    path = "_" + sign + ".png"
    Picture.create(signs, path, sign)
