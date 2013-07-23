from Myro import *
init("sim")

# Make a graphics window to show the pictures in
win = Window('Video Stream', 427, 266)

# Set the picture size to be smaller, better performance
setPicSize("small")

# Open up a joystick controller to move the robot around
joystick()

# Define the colors we'll be using to modify the pictures
blue = (112, 150, 158)
black = (0, 51, 76)
red = (217, 26, 33)
yellow = (252, 227, 166)

# Stream while the graphics Window is open
while win.isVisible():
    pic = takePicture('gray')
    
    # If there's something close to the camera (IR sensor), change the image!
    if (getObstacle('center') > 2000):
        # Go through all the pixels and edit their color based on their brightness
        for pixel in getPixels(pic):
            gray = getGray(pixel)
            if gray >= 180:
                setRGB(pixel, yellow)
            elif  gray>= 120 and gray <= 180:
                setRGB(pixel, blue)
            elif gray >= 60 and gray <= 120:
                setRGB(pixel, red)
            else:
                 setRGB(pixel, black)

    pic.undraw()               # Clear the previous picture
    pic.draw(win)              # Draw the new picture, "streams" : )
