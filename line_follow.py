from Myro import *
init()

# To stop the Scribbler, wave your hand/something in front of the fluke
while getObstacle('center') < 6300:
    # Get the reading from the line sensors on the bottom of Scribbler
    left, right = getLine()
    
    # If both left and right sensors are on track
    if left == 1 and right == 1:
        motors(-.1, -.1)
        
    # If just the right is on track, turn left
    elif right == 1:
        motors(.1,-.1)
        
    # If just the left is on track, turn right
    elif left == 1:
        motors(-.1,.1)
        
    # If both are off track, go backwards in a random direction.
    # randomNumber returns a number between 0 and 1, so I scale that to go slower
    elif left == 0 and right == 0:
            motors(.1*randomNumber(),.1*randomNumber())
  
# When it's done, stop and beep happily          
stop()
beep(.1,600)
beep(.1,650)
beep(.1,700)
beep(.1,750)
beep(.1,800)
beep(.1,850)
