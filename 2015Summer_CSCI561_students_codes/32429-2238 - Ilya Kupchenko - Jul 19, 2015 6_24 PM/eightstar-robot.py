# IMPORTANT! For this program, be sure to also download the background image at
# https://raw.github.com/CSavvy/python/master/draw_shapes.py
# and put it in the same folder that you put this program!!

from Myro import *
init("com19")
penUp()

from Graphics import *

forward(3,1.0)

penDown()

a1 = 360/8

turnBy(a1/2)

for i in xrange(360/a1):
  forward(3, .6)
  turnBy(180-a1)
  forward(3, .6)
  turnBy(-(180-2*a1))
  
turnBy(a1*1.2)

motors(0,5)
wait(6.8)
stop()



