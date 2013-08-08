from Myro import *
init("sim")

setPictureSize("small")
autoCamera()


#'''
#chase blue setting
ylow = 0
yhigh = 255
ulow = 170 #130 for the straw # originally 134
uhigh = 250 # up to 158, really 145, 157 for the straw #142 originally
vlow = 90 # down to 109, really 114, 110 for the straw #114 originally
vhigh = 120 #really up to 123, 127 for the straw #121 originally
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
#'''
s = 2
left = -s
right = s
time = 0.5/s
c = 0
motors(5,-5,0.4*2)
while True:
    wait(2)
    print(getIR())
    while getIR() == [1, 1]:
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
    
        print("Number of pixels of interest color: ", num)
        xavg = xsum / num
        print("Average x position of interest color: ", xavg)
        yavg = ysum / num
        #print(yavg)
        #continue #uncomment this line to prevent motion
        if num > 200: #there are enough pixels of the color of interest
            if xavg < 90:# the object is to the left
                #turnBy(-10)

                left = -s
                right = s
                time = 0.5/s
                motors(left,right,time)
            elif xavg > 190:# the object is to the right
                #turnBy(10)
                left = s
                right = -s
                time = 0.5/s

                motors(left,right,time)

            else:#the object is ahead
                forward(s,0.8)
                #beep(0.1, 600)
        else:#no object of interest is detected
            print(left,right,time)
            motors(left,right,time)
            #beep(0.1, 670, 690)

