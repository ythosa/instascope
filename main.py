# -*- coding: utf-8 -*-
from libs.pic import Picture
from libs.horoscope import Horoscope

signs = Horoscope.symbols

# Generate pictures for each sign
for sign in signs.keys():
    path = "_" + sign + ".png"
    Picture.create(signs, path, sign)


# Picture.create(signs, "1111.png", "cancer")
