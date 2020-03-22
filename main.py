# -*- coding: utf-8 -*-
from InstagramAPI import InstagramAPI
from libs.pic import Picture

photo_path = "back.png"

Picture.create(photo_path, "virgo")

InstagramAPI = InstagramAPI("_ganjaclub", "lolka228")
InstagramAPI.login()  # login

caption = "Sample photo"
InstagramAPI.uploadPhoto(photo_path, caption=caption)
