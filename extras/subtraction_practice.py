from Myro import *
from random import randint

# Keep track of how many questions they answered, and how many were correct
question_number = 0
correct = 0

playing = True
while playing:
    # Print a blank line so the output window looks nicer...
    print(" ")

    # Get two random numbers for them to add or subtract. can be - - (so add)
    num1 = randint(1, 100)
    num2 = randint(-100, 100)

    # Print out the question. They're subtraction problems
    question = "What is " + str(num1) + " - " + str(num2) + "? "
    print(question)

    # I use the try/except so there's no error message if they close the window...
    try:
        response = int( ask(question) )
    except:
        print("You chose to quit")
        break

    print("Your answer: ", response)

    # If they got it right on their first try
    if response == (num1 - num2):
        correct += 1

    # Keep asking them until they get it correct
    while response != (num1 - num2):
        question = "Incorrect. Please try again. What is " + str(num1) + " - " + str(num2) + "? "
        print(question)

        try:
            response = int( ask(question) )
        except:
            print("You chose to quit")
            playing = False
            break

        print("Your answer: ", response)

    # They got it right! (well, they kind of have to...)
    print("Correct!")
    question_number += 1

# Print a message when they're quitting
print("Game finished.")
print("Number of questions answered: ", question_number)
print("Number of questions answered correctly on first try: ", correct)
