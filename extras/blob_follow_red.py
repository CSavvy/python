from Myro import *
init("com9")

setPictureSize("small")
autoCamera()

#sets to "red" based on yuv color scheme
ylow = 0
yhigh = 255
ulow = 123
uhigh = 133
vlow = 138
vhigh = 183
xsum = 0
ysum = 0
num = 0

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
        if u >= ulow and u <= uhigh and v >= vlow and v <= vhigh:
            num = num + 1
            xsum += getX(pixel)
            ysum += getY(pixel)
            setRed(pixel, 255)
            #print(rgb2yuv(r,g,b))
        else:
            #print(rgb2yuv(r,g,b))
            setBlue(pixel, 255)


    print(num)
    xavg = xsum / num
    print(xavg)
    #yavg = ysum / num
    #print(yavg)

    if num > 1500:
        if xavg < 150:
            turnBy(10)
        elif xavg > 300:
            turnBy(-10)
        else:
            forward(1,1)
            beep(0.1, 600)
    else:
        beep(0.1, 500, 600)

