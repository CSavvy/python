from Myro import *
init()

# The notes I'll be using to play Mary Had a Little Lamb
G4 = 783.99
A4 = 880
B4 = 987.77

# Drive slowly across the page with music lines
backward(.1)

# To stop the Scribbler, wave your hand/something in front of the fluke
while getObstacle('center') < 6300:
    left, right = getLine()

    # Beep a different tone depending on what code is present (left, right, both)
    if left == 1 and right == 1:
        beep(0.32,G4)
    elif right == 1:
        beep(0.32,B4)
    elif left == 1:
        beep(0.32,A4)
    # Don't make any noise if Scribbler is off the track

# When it's done, stop Scribbler
stop()


# If you just want to play Mary had a little lamb without driving, uncomment the
# song below and comment out the code above (except from and init, of course)
"""beep(.5, B4)
beep(.5, A4)
beep(.5, G4)
beep(.5, A4)

beep(.5, B4)
wait(.05)
beep(.5, B4)
wait(.05)
beep(1, B4)

beep(.5, A4)
wait(.05)
beep(.5, A4)
wait(.05)
beep(1, A4)

beep(.5, B4)
wait(.05)
beep(.5, B4)
wait(.05)
beep(1, B4)
wait(.05)

beep(.5, B4)
beep(.5, A4)
beep(.5, G4)
beep(.5, A4)

beep(.5, B4)
wait(.05)
beep(.5, B4)
wait(.05)
beep(1, B4)

beep(.5, A4)
wait(.05)
beep(.5, A4)
beep(.5, B4)
beep(.5, A4)
beep(1, G4)"""
