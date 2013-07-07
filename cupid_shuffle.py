def cupid():
    steptime = .4
    kick_angle = -35

    for i in range(4):
        forward(1, steptime)
        wait(steptime)
    for i in range(4):
        backward(1, steptime)
        wait(steptime)
    for i in range(2):
        turnBy(kick_angle)
        wait(.2)
        turnBy(-kick_angle)
        wait(.2)
        kick_angle = -kick_angle
    wait(.5)
    turnBy(-90)

from Myro import *
init()

# NOTE: be sure to download the wav file at https://github.com/CSavvy/python/blob/master/shuffle2.wav
s = makeSound("shuffle2.wav")
for j in range(1): #set number of loops here
    c = s.Play(0, 32000)
    wait(5)
    cupid()
    wait(.5)
    cupid()
