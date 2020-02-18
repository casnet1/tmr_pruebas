#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep
from PIL import Image

lcd = Screen()

logo = Image.open('./EV3_BMP/Smile.bmp')
lcd.image.paste(logo, (0,0))
lcd.update()
sleep(5) # when running from Brickman, need time to admire image