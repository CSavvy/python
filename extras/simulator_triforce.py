from Myro import *
init("sim")
r = -60
penDown()
s = 5
t = 2/s
for i in range(1):
    forward(s,t)
    turnBy(r)
    forward(-s,t)
    turnBy(r)
    forward(s,t)

    turnBy(-r)
    forward(s,t)
    turnBy(r)
    forward(-s,t)
    forward(-s,t)
    turnBy(r)
    forward(s,t)

    forward(s,t)
    turnBy(r)
    forward(-s,t)
    #move away to showcase drawing
    turnBy(-r)
    forward(s,t)
