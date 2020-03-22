from InstagramAPI import InstagramAPI

InstagramAPI = InstagramAPI("_ganjaclub", "lolka228")
InstagramAPI.login()  # login

photo_path = 'fon.jpg'
caption = "Sample photo"
InstagramAPI.uploadPhoto(photo_path, caption=caption)