# Import Myro (as always)
from Myro import *

# Connect to the robot
init("sim")

# This is the array that will hold all the pictures as Scribbler spins
gif_images = []

# Set camera modes to make capturing faster
setPicSize("small")
autoCamera()

# Now have Scribbler spin in a circle and take a picture with each small turn
for i in xrange(35):
    print(i)
    #setLEDFront(1) # "Flash" the LED like a camera (1 to turn on, 0 to turn off)
    p = takePicture() # Take the picture
    gif_images.append(p) # Add that picture to the gif_images array
    #setLEDFront(0) # Turn the LED off
    #wait(.5)
    turnBy(10)    # Turn left by a small amount (makes a complete circle in end)
    #wait(.5)
    #beep(.1, 700)    # Also beep to let users know it's taken a picture

# Print the status of the program
print('Done capturing photos')
print('Making the gif')

# Save the gif file. scribbler_360 is the filename, you can change it if you want
savePicture(gif_images, 'scribbler_360.gif')

# Beep to hear that it's done
#beep(.1, 750)
#beep(.1,800)
#beep(.1,850)
