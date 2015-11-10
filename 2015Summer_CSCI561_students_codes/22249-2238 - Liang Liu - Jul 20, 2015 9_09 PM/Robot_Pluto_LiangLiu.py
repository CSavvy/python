from Myro import *
init("/dev/tty.Fluke2-024E-Fluke2")

# full circle

beep(1,660)
beep(3,440)
motors(0.7, 0.08, 7.8)

# left heart
turnRight(1,0.35)
forward(0.5,0.7)
turnRight(1,0.15)
motors(0.8,-0.33,2)
turnLeft(1,0.7)
motors(0.8,-0.33,2)
turnRight(1,0.19)
forward(0.5,0.79)

'''
#
#to P
beep(1,440)
beep(3,660)
forward(0.5,1.3)
turnRight(0.5,2)
beep(1,660)
beep(3,440)


#P
forward(0.5, 0.6)
turnRight(0.5,1.3)
motors(0.8,-0.55,2)

# to L
beep(1,440)
beep(3,660)
backward(0.5,0.3)
turnLeft(0.5,1.5)
backward(0.5,0.3)
beep(1,660)
beep(3,440)

#L
forward(0.5, 0.6)
turnLeft(0.5,1.3)
forward(0.5,0.3)

#to U
beep(1,440)
beep(3,660)
forward(0.5,0.1)
turnRight(0.5,1.3)
backward(0.5,0.6)
beep(1,660)
beep(3,440)




#U
forward(0.5,0.45)
motors(-0.56,0.8,1.9)
forward(0.5,0.45)

#to T
beep(1,440)
beep(3,660)
turnRight(0.5,1.3)
forward(0.5,0.2)
beep(1,660)
beep(3,440)

#T
forward(0.5,0.3)
backward(0.5,0.15)
turnRight(0.5,1.3)
forward(0.5,0.7)

#to O
beep(1,440)
beep(3,660)
turnLeft(0.5,1.3)
forward(0.5,0.3)
turnLeft(0.5,1.3)
forward(0.5,0.3)
beep(1,660)
beep(3,440)

#O
forward(0.5,0.2)
motors(0.8,-0.5,2.0)
forward(0.5,0.2)
motors(0.8,-0.5,2.0)

#end
beep(1,440)
beep(3,660)
'''