# -*- coding: utf-8 -*-
# author: Ethosa
from random import randint, choice

from collections import namedtuple

from saya import Vk  # VK API
import requests  # download images


class Meme:
    @staticmethod
    def get():
        """
        Gets random picture from 4ch and write it in the file.
        """
        publ = namedtuple('public', ['owner_id', 'album_id'])
        publics = [
            # List albums of memes
            publ(-45745333, '262436923'),
            publ(-45745333, '262436923'),
            publ(-176864224, 'wall'),
            publ(-29606875, 'wall'),
            publ(-144918406, 'wall')
        ]
        choiced_public = choice(publics)
        vk = Vk(token="99a11d3599a11d3599a11d354099ce5222999a199a11d35c78d50e3779b82feb9455cee")
        photos = vk.photos.get(  # Gets all photos from album
            owner_id=choiced_public.owner_id, album_id=choiced_public.album_id,
            rev=randint(0, 1), offset=randint(0, 500), count=1000)
        photo = choice(photos["response"]["items"])  # Gets random photo from photos list.
        w = h = 0
        url = ""
        for size in photo["sizes"]:  # Gets max photo size.
            if size["width"] > w and size["height"] > h:
                w = size["width"]
                h = size["height"]
                url = size["url"]
        if url:
            # Write photo in file, if available.
            with open("meme.png", "wb") as f:
                f.write(requests.get(url).content)
