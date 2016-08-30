import numpy as np
from PIL import Image, ImageDraw, ImageFont
from skimage import transform as tf

def create_captcha(num, shear = 0, size =(100,24)):
    im = Image.new("L", size, "black")
    draw = ImageDraw.Draw(im)
    draw.show()
    
create_captcha(65)
