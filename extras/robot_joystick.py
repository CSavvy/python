# This program lets a user control a robot with a joystick and
# test taking pictures and making the robot beep


# This function checks if a point is inside the joystick circle
def checkIfInCircle(x, y):
    from math import *
    if fabs((x - 250)*(x - 250) + (y - 250)*(y - 250)) <= 245*245:
        return True
    else:
    	return False

def main():
    # Import the Myro and Graphics libraries, and connect to the robot
    from Myro import *
    from Graphics import *
    init()
    
    # Create the window that will have the joystick
    win = Window('Robot Joystick', 700, 500)
    win.setBackground(Color('gray'))

    # Create the joystick circle
    cir = Circle(Point(250, 250), 245)
    cir.setWidth(3)
    cir.setFill(Color('white'))
    cir.draw(win)
    
    # Draw a point in the middle of the circle for reference
    cir = Circle(Point(250, 250), 3)
    cir.setWidth(1)
    cir.draw(win)

    # Make some "buttons" to the side of the joystick with more actions, like beeping.
    # I handle when they're clicked by checking the location of a mouse click, in the
    # while loop below.
    rect = Rectangle(Point(550,75), Point(650,125))		# Draw a rectangle around it
    rect.setFill(Color('green'))
    rect.draw(win)
    text = Text(Point(600, 100), "Beep")                 # Make the beep label
    text.draw(win)

    rect = Rectangle(Point(550,175), Point(650,225))
    rect.setFill(Color('red'))
    rect.draw(win)
    text = Text(Point(600, 200), "Picture")
    text.draw(win)

    # Constantly get the mouse position and draw a circle
    center = Point(250, 250)
    direction = center									# The direction to move in
    l = Line(center, center)
    while win.isVisible():
        x, y = getMouseNow()                            # Get mouse now (don't wait for click)
        if getMouseState() == "down":                   # Mouse needs to be held down
            # Use the click's location to see what they clicked on
            
            # Drive
            if x >= 0 and y >= 0 and checkIfInCircle(x, y):
                direction = Point(center[0] - x, center[1] - y)
                move(direction[1]/245.0, direction[0]/245.0)
                l.undraw()
                l = Line(center, (x, y))
                l.setWidth(3)
                l.draw(win)
            # Beep
            elif x >= 550 and y < 150:
                l.undraw()
                move(0,0)
       	        beep(.5, 880)
                beep(.5, 600)
                beep(1, 400)
            # Take a picture and save it as a .png on your computer
            elif x >= 550 and y > 150 and y <= 250:
                motors(0,0)
                text1 = Text(Point(600, 400), "Taking Picture in")
                text1.draw(win)
                text = Text(Point(615, 425), "3...")
                beep(.5, 600)
                text.draw(win)
                wait(1)
                text.undraw()
                text = Text(Point(615, 425), "2...")
                beep(.5, 600)
                text.draw(win)
                wait(1)
                text.undraw()
                text = Text(Point(615, 425), "1...")
                beep(.5, 600)
                text.draw(win)
                wait(1)
                text1.undraw()
                text.undraw()
                text = Text(Point(615, 425), "Capturing Photo...")
                beep(.7, 800)
                text.draw(win)
                pic = takePicture()
                beep(.2, 700)
                text.undraw()
                # Save the picture file
                savePicture(pic, "scribbler_picture.png")
        # If mouse isn't pressed down, clear the joystick line
        else:
            l.undraw()
            move(0, 0)
        wait(0.05)

main()