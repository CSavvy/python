# This code makes the robot to draw a heart !
# Author: Mohammad Ali, Motie Share
from Myro import*
init("/dev/tty.Fluke2-0214-Fluke2")

setName("RED BOY")
print("Now my name is", getName())


#forward(1,0.3)
#wait(2)
turnRight(1,0.3)
wait(2)
forward(.4,1)
wait(2)
motors(-0.5,1,2)
wait(2)
turnRight(1,.85)
wait(2)
motors(-0.5,1,2)
wait(2)
forward(.4,1)

beep(0.5,400)
