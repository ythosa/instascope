from InstagramAPI import InstagramAPI
# -*- coding: utf-8 -*-
from libs.pic import Picture

InstagramAPI = InstagramAPI("_ganjaclub", "lolka228")
InstagramAPI.login()  # login

photo_path = 'fon.jpg'
caption = "Sample photo"
InstagramAPI.uploadPhoto(photo_path, caption=caption)
Picture.create("filename.png", "virgo")
