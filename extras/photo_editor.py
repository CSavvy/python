# This program lets you take a picture with your scribbler, then draw on it and save the new, annotated picture
from Myro import *
from Graphics import *
init()

# Make a graphics window to show the pictures in
win = Window('Photo Editor', 1480, 800)

# Define the colors we'll be using to draw on the picture
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

# Set default color to be red
color = red

# Take a picture with the robot. We'll edit it later
pic = takePicture()

# These functions connect to the buttons, and set the color to draw with
def redPen(o, e):
    global color
    color = red

def bluePen(o, e):
    global color
    color = blue

def greenPen(o, e):
    global color
    color = green

def yellowPen(o, e):
    global color
    color = yellow

def blackPen(o, e):
    global color
    color = black

def whitePen(o, e):
    global color
    color = white

# Make a title for all the color buttons
text = Text(Point(1330, 25),"Colors")
text.setFill(Color('black'))
text.draw(win)

# Set up buttons to change the pen color
button = Button(Point(1330, 50), "Red")
button.draw(win)
button.connect("click", redPen) # When the button is pressed, the redPen function is called

button = Button(Point(1330, 80), "Green")
button.draw(win)
button.connect("click", greenPen)

button = Button(Point(1330, 110), "Blue")
button.draw(win)
button.connect("click", bluePen)

button = Button(Point(1330, 140), "Yellow")
button.draw(win)
button.connect("click", yellowPen)

button = Button(Point(1330, 170), "Black")
button.draw(win)
button.connect("click", blackPen)

button = Button(Point(1330, 200), "White")
button.draw(win)
button.connect("click", whitePen)


# Put the picture taken by the robot in the graphics window, and let users draw on it!
pic.draw(win)

while win.isVisible():
    # Get the current mouse location
    x, y = getMouseNow()
        
    # Check that the mouse is pressed down and over the picture
    if getMouseState() == "down" and x >= 0 and x <= 1280 and y >= 0 and y <= 1280:
        # Draw red where mouse is clicked to annotate/draw
        # These two for loops make it draw a larger circle around the mouse click, not just one point
        for i in range(8):
            for j in range(8):
                # This if statement and continue just make it into a circle, not a square
                if ((i*i + j*j) > 49):
                    continue
                # Set pixels to fill the circle
                setRGB(getPixel(pic, x+i, y+j), color)
                setRGB(getPixel(pic, x+i, y-j), color)
                setRGB(getPixel(pic, x-i, y+j), color)
                setRGB(getPixel(pic, x-i, y-j), color)

# Now that they've closed the window, ask them for a filename to save the picture
filename = ask("What name do you want to save the picture as? (do not include the extension)")
savePicture(pic, filename + ".png")