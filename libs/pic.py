from PIL import Image, ImageDraw, ImageFont

from horoscope import Horoscope
from meme import Meme

# take a horoscope list
horoscope_list = Horoscope.get_horoscope()
print(horoscope_list['leo'])
# take a meme
# Meme.get()
#
#
# fon = Image.new('RGB', (1080, 1920), color='#FFFFFF')
# font = ImageFont.truetype(r'data\DroidSans.ttf', 140)
# meme = Image.open('meme.png', 'r')
# meme = meme.resize((1000, 1000))
#
# fon.save('fon.jpg')
# story_img = ImageDraw.Draw(fon)
#
# story_img.text((100, 100), horoscope_list['leo'][0], align="left", font=font, fill="#000000")
# fon.paste(meme, (40, 880))
#
# fon.show()
