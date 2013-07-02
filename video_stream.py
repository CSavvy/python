from Myro import *
init("com7")

# Make a graphics window to show the pictures in
win = Window('Video Stream', 427, 266)

# Set the picture size to be smaller, better performance
setPicSize("small")
autoCamera()

# Open up a joystick controller to move the robot around
joystick()

while win.isVisible():         # Stream while the graphics Window is open
    pic = takePicture("gray")        # Stream in grayscale, faster
    pic.undraw()               # Clear the previous picture
    pic.draw(win)              # Draw the new picture, "streams" : )
