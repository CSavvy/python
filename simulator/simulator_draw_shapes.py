# IMPORTANT! For this program, be sure to also download the background image at
# https://raw.github.com/CSavvy/python/master/draw_shapes.py
# and put it in the same folder that you put this program!!

from Myro import *
init("sim")
penDown()

from Graphics import *

win = Window('Draw Shapes with Scribbler', 500, 500)
background = makePicture("shape_gui_background.png")
background.draw(win)

while win.isVisible():
    x, y = getMouse()

    if x < 250 and y < 250:
        print('Drawing a Square')
        for i in xrange(4):
            forward(5, .6)
            #wait(1)
            turnBy(90)
            #wait(2)
            #wait(1)
    elif x < 250 and y >= 250:
        print('Drawing a Triangle')
        forward(5, 0.6)
        turnBy(60)
        stop()
        forward(-5, 0.6)
        turnBy(60)
        stop()
        forward(5, 0.6)
    elif x >= 250 and y < 250:
        print('Drawing a Circle')
        motors(0,5)
        wait(3.8)
        stop()
    elif x >= 250 and y >= 250:
        print('Drawing a Heart')
        penDown()
        circle = 4.3
        line = 2.8
        motors(-.5,2.4)
        wait(circle)
        forward(1,line)
        turnBy(-98)
        forward(1,line)
        motors(-.5,2.4)
        wait(circle)
        stop()

    wait(0.05)
