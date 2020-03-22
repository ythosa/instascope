# -*- coding: utf-8 -*-
from InstagramAPI import InstagramAPI
from libs.pic import Picture

path = "back.png"

Picture.create(path, "virgo")

# --- Auth --- #
InstagramAPI = InstagramAPI("_ganjaclub", "lolka228")
InstagramAPI.login()  # login

# --- Upload --- #
InstagramAPI.uploadStoryPhoto(path)
