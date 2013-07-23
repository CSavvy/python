# The scribbler acts as a vacuum, cleaning two squares. A reflective square must be
# above carpet, or something unreflective (ex a whiteboard).

from Myro import *
init()

# These boolean variables store if a square is clean or dirty, and if a square is visited
# even if a square is clean Scribbler must visit it to check.
left_square_clean, right_square_clean, left_visited, right_visited = False, False, False, False

# Use randomness (flip coin) to determine if a square is clean or dirty
if flipCoin() == "heads":
    left_square_clean = True

if flipCoin() == "heads":
    right_square_clean = True

# Run until Scribbler has visited both squares, and cleaned them if necessary
while not left_visited or not right_visited:
    # Get the reading from the line sensors on the bottom of Scribbler to determine where it is
    left, right = getLine()
    print("STATUS: Left clean: " + str(left_square_clean) + ". Right clean: " + str(right_square_clean))

    # If both left and right sensors are on carpet ("left square")
    if left == 1 and right == 1:
        print("I'm on the carpet (left)")
        left_visited = True
        
        # Clean if necessary!
        if not left_square_clean:
            print("It's dirty... Time to clean!")
            motors(-1,1, 9.54)
            left_square_clean = True
            beep(1, 500)
            
        # Go to the other square if Scribbler hasn't already
        if not right_visited:
                forward(1, 2)

    # If both are on whiteboard ("right square")
    if left == 0 and right == 0:
        print("I'm on the whiteboard (right)")
        right_visited = True
        
        # Clean if necessary!
        if not right_square_clean:
            print("It's dirty... Time to clean!")
            motors(-1,1, 9.54)
            right_square_clean = True
            beep(1, 700)
            
        # Go to the other square if Scribbler hasn't already
        if not left_visited:
                backward(1, 2)

print("I'm done cleaning!!!!!!!!!!!!!")
beep(.3,600)
beep(.3,700)
beep(.3,800)
