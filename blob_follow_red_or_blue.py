'''
To adjust the color settings, it is best to uncomment
one print line to see which yuv values to bound for that
specific color and uncomment the "continue" line to stop movement
so that you can focus on picking the color of interest.
'''
from Myro import *
init()

setPictureSize("small")
autoCamera()



#chase blue setting
ylow = 0
yhigh = 255
ulow = 134
uhigh = 142
vlow = 114
vhigh = 121
xsum = 0
ysum = 0
num = 0
'''
#chase red setting
ylow = 0
yhigh = 255
ulow = 122
uhigh = 134
vlow = 143
vhigh = 183
xsum = 0
ysum = 0
num = 0
'''


c = 0
while True:
    num = 1
    xsum = 0
    ysum = 0
    p = takePicture()


    show(p)
    for pixel in getPixels(p):
        color = getColor(pixel)
        r = getRed(pixel)
        g = getGreen(pixel)
        b = getBlue(pixel)


        y, u, v = rgb2yuv(r,g,b)
        #this is the color of interest, highlighted in red
        if u >= ulow and u <= uhigh and v >= vlow and v <= vhigh:
            num = num + 1
            xsum += getX(pixel)
            ysum += getY(pixel)
            setRed(pixel, 200)
            #print(rgb2yuv(r,g,b))#
        else: #colors that are not of interest, highlighted in blue
            '''
            c += 1
            if (c % 25 == 0):
                print(rgb2yuv(r,g,b))#
            '''
            #print(rgb2yuv(r,g,b))
            setBlue(pixel, 200)

    print("The number of pixels of the color of interest: ", num)
    xavg = xsum / num
    print("The average pixel x position of the color of interest: ", xavg)
    yavg = ysum / num
    #print(yavg)
    #continue #uncomment this line to prevent motion
    if num > 1000: #there are enough pixels of the color of interest
        if xavg < 150:#the object is to the left
            turnBy(10)
        elif xavg > 300:#the object is to the right
            turnBy(-10)
        else:#the object is ahead
            forward(1,1)
            beep(0.1, 600)
    else:#no object of interest is detected
        beep(0.1, 500, 600)

