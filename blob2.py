
from Myro import *

# Connect to the robot
#init("com9")
ymin = 255
umin = 255
vmin = 255
ymax = 0
umax = 0
vmax = 0
ulow = 121
uhigh = 133
vlow = 134
vhigh = 183
xsum = 0
ysum = 0
num = 0
setPictureSize("small")
autoCamera()
for i in range(4):
    po = takePicture()
    p = copyPicture(po)
    prev_pixel = getPixel(p, 0, 0)

    show(p)
    for pixel in getPixels(p):
        color = getColor(pixel)
        r = getRed(pixel)
        g = getGreen(pixel)
        b = getBlue(pixel)


        y, u, v = rgb2yuv(r,g,b)
        if u >= ulow and u <= uhigh and v >= vlow and v <= vhigh:
            num = num + 1
            xsum += getX(pixel)
            ysum += getY(pixel)
            setBlue(pixel, 255)
            #  print(rgb2yuv(r,g,b))#
        else:
        #print(rgb2yuv(r,g,b))#
            setRed(pixel, 255)
        prev_pixel = pixel

    print(num)
    print(xsum / num)
    print(ysum / num)
    #win = Window('Video Stream', 427, 266)

    #po.draw(win)
    if num > 10000:
        if xsum / num < 170:
            turnBy(15)
        elif xsum / num > 330:
            turnBy(-15)
        else:
            forward(1,.3)
            beep(0.5, 600)
    else:
        beep(0.5, 500)
