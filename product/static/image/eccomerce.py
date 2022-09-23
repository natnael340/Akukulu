from PIL import Image
import numpy as np
from matplotlib import pyplot

b_w = 300
b_h = 300

img = Image.open("main.jpg")

w,h = img.size
bgb = np.full((b_w,b_h,3), 255, dtype='int')
bga = np.zeros((b_w,b_h,4), dtype='int') 
bga[:,:,:-1] = bgb
back = Image.new("RGBA", (b_w,b_h),(255,255,255,0))
if w>h:
    h = round(b_w*(h/w))
    w=b_w
else :
    w=round(b_h*(w/h))
    h=b_h
img = img.resize((w,h), Image.ANTIALIAS)
offset = ((b_w-w)//2,(b_h-h)//2)
back.paste(img, offset)
pyplot.imshow(back)
#back.save("mainbg.png", "PNG")
