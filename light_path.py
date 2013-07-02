####################
# Connect to Robot #
####################
from Myro import *
init("com3")

################
# Drive a Path #
################
def drive(path):
 # iterate through path string, and drive!
 for s in path:
     if s == 'L':
         turnBy(-90)
     elif s == 'C':
         forward(1, 1)
     elif s == 'R':
         turnBy(90)
     # For pause
     wait(.5)

##################
# Determine Path #
##################

# My path string! I chose to use a string because it's easy to add to and iterate through
path = ""

L, C, R = getLight()
l, c, r = L, C, R
threshold = 5000
# Listen to light sensors and determine path
while (getObstacle('center') < 6300 ): #check fluke IR, stop if wave in front
    #Get lights
    L, C, R = getLight()
    print("L %d C %d R %d sum %d" %(L, C, R, L + C + R))
    if c-C > threshold: #center brightened
        beep(.5,700)
        path += 'C'
        print("C ", C)
    elif l-L > threshold: #left brightened
        beep(.5,600)
        path += 'L'
        print("L ", L)
    elif r-R > threshold: #right brightened
        beep(.5,800)
        path += 'R'
        print("R ", R)
    l = L; c = C; r = R
    wait(1) #pause 1 second between checks

beep(.3, 500)
wait(2)
drive(path)
beep(.3,600)
beep(.3,700)
beep(.3,800)
