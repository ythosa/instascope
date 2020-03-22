<<<<<<< HEAD
from InstagramAPI import InstagramAPI
=======
# -*- coding: utf-8 -*-
from libs.pic import Picture
>>>>>>> 1be61277d29a406ee86aeffce6017dfaa6f112f2

InstagramAPI = InstagramAPI("_ganjaclub", "lolka228")
InstagramAPI.login()  # login

<<<<<<< HEAD
photo_path = 'fon.jpg'
caption = "Sample photo"
InstagramAPI.uploadPhoto(photo_path, caption=caption)
=======
Picture.create("filename.png", "virgo")
>>>>>>> 1be61277d29a406ee86aeffce6017dfaa6f112f2
