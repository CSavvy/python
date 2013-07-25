# Import Myro library and connect to the robot
from Myro import *
init("/dev/tty.Fluke2-0216-Fluke2")

# Draws a Circle
#motors(.1,.8) # Different way's to move, like motors or forward
forward(1)
rotate(1)
wait(8)
stop()		   # Remember to call stop if you don't specify a time to move

# Turn, because we're going to inscribe a triangle in the circle we just drew!
turnBy(60)

# Draws a Triangle inside that circle!
forward(1,.9)
turnBy(120)
forward(1,.9)
turnBy(120)
forward(1,.9)