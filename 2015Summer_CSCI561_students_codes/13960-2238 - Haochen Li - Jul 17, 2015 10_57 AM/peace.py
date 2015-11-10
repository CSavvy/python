## This program will let Scribbler draw peace logo
## Enjoy!

from Myro import *
init("/dev/tty.Fluke2-0220-Fluke2")

## draw circle
wait(3)
motors(-0.2, 0.7, 6)

## turn 90 degrees
## because of constant errors rotate 88 degrees instead
turnBy(88)

r = 0.49
## draw central line
forward(0.5, 2*r)
backward(0.5, r)

## draw 50 degree lines
turnBy(50)
forward(0.5, r)
backward(0.5, r)
turnBy(-100)
forward(0.5, r)
backward(0.5, r)

