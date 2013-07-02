# IMPORTANT! For this program, be sure to also download the background image at
# www.github.com/CSavvy/python/blob/master/shape_gui_background.png
# and put it in the same folder that you put this program!!


# Import Myro library and connect to the robot
from Myro import *
init("/dev/tty.Fluke2-0216-Fluke2")

# We also need to import the graphics library!
from Graphics import *

# Print the current battery level
print("Battery level:", getBattery())

# Make a graphics window with the title below and dimensions 500x500
win = Window('Draw Shapes with Scribbler', 500, 500)

# Now set the window's background with a picture.
# Remember to have this picture in the same folder as this program!!
background = makePicture("shape_gui_background.png")

# Draw the background picture on the graphics Window
background.draw(win)

# Run a loop while the window is open to keep getting where the user clicks to draw shapes
while win.isVisible():
    # Wait for them to click, and store the x and y coordinates of their click in x and y
    x, y = getMouse()
    
    # Now analyze where they clicked by checking x and y location, and draw appropriate shape
    if x < 250 and y < 250:
        print('Drawing a Square')
        forward(1, 1)
        turnBy(90)
        forward(1, 1)
        turnBy(90)
        forward(1, 1)
        turnBy(90)
        forward(1, 1)
        turnBy(90)
    elif x < 250 and y >= 250:
        print('Drawing a Triangle')
        forward(1,.9)
        turnBy(120)
        forward(1,.9)
        turnBy(120)
        forward(1,.9)
    elif x >= 250 and y < 250:
        print('Drawing a Circle')
        motors(.1,.8)
        wait(9)
        stop()
    elif x >= 250 and y >= 250:
        print('Drawing a Heart')
        motors(0,1)
        wait(4)
        forward(1,1)
        turnLeft(1,.65)
        forward(1,1)
        motors(0,1)
        wait(4)
        stop()
        
    # Wait a small amount before checking again
    wait(0.05)
