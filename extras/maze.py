# Escape the maze!
# Adapted from http://wiki.roboteducation.org/wiki/images/7/72/Escape.pyw

from Myro import *
init()

def evade():
    #Displeasure
    setLEDFront(1)
    beep(0.1,800)
    beep(0.15,550)
    setLEDFront(0)

    #Avoidance
    forward(1,0.4)
    turnLeft(1,0.25)


free = False
while (not free):
        # Head "backwards" unless something appears
        # in front of us or 8 seconds are up.
        for seconds in timer(8):
            print('timer: ', seconds)   # Just print out the timer to see
            left,right = getIR()        # Get the IR sensor readings
            backward(0.65)
            if (left == 0 or right == 0 or getStall()): # Stop if there's something in front if IR or robot's stopped
                stop()
                print("IR sensor hit!")
                evade()
                break
        else:                   # If Scribbler successfully drives for 8 seconds without hitting something, it's free!
            print("I'm free!")
            free = True

# We've escaped the maze, so stop the robot
stop()

