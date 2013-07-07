from Myro import *
init()
Ambient = getLight("center")
def normalize(v):
    if v > Ambient:
        v = Ambient
    return 1.0 - v/Ambient

def main():
    while True:
        C = getLight("center")
        backward(normalize(C))
        L = getLight("left")
        R = getLight("right")
        print(getLight())
        turn = normalize(L) - normalize(R)
        scale = 4
        print(turn*90*scale)
        if abs(turn*90*scale) < 90:
            rotate(turn*90*scale)
        else:
            rotate(turn*90)
            print("scale")
        wait(.1)
main()
