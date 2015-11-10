# Import Myro library and connect to the robot
from Myro import *
init("com4")

def draw_hypocycloid():
    wait_time = 2
    speed_factor = 1
    turn_time = 0.5
    
    motors(0.0, 0.5)
    wait(wait_time)
    stop()
    turnLeft(0.5, 0.50)
    
    motors(-0.5, 0.0)
    wait(wait_time)
    stop()
    turnLeft(0.5, 0.25)
    
    motors(0.0, 0.5)
    wait(wait_time)
    stop()
    turnLeft(0.5, 0.25)
    
    motors(-0.5, 0.0)
    wait(wait_time)
    stop()
    
print("Battery voltage: " + str(getBattery()))
draw_hypocycloid()
