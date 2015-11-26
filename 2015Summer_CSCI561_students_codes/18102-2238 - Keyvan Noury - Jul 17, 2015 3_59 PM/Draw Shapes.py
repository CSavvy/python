from Myro import *
init("com4")

from Graphics import *

win = Window('Draw What You Want', 500, 500)

background = makePicture("shapes.png")

background.draw(win)

# Run a loop while the window is open to keep getting where the user clicks to draw shapes
while win.isVisible():
    # Wait for them to click, and store the x and y coordinates of their click in x and y
    x, y = getMouse()
    
    # Now analyze where they clicked by checking x and y location, and draw appropriate shape
    if x < 250 and y < 250:
        print('Drawing a Heart')
        motors(0,0.5)
        wait(3)
        forward(0.5,0.5)
        turnLeft(0.5,.45)
        forward(0.5,0.5)
        motors(0,0.5)
        wait(3)
        stop()
    elif x >= 250 and y < 250:
        print('Drawing a Circle')
        motors(.1,.8)
        wait(4)
        stop()
        
    # Wait a small amount before checking again
    wait(0.05)
