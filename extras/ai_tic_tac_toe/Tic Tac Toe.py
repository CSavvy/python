# Adapted from http://inventwithpython.com/chapter10.html
# Uses AIMA code under the MIT license http://opensource.org/licenses/MIT

# Tic Tac Toe game using AI and Myro
from Myro import *
from Graphics import *
import random
from games import *

# Make the board window
win = Window("Tic Tac Toe!!!!", 600, 600)
win.setBackground(Color('white'))

def drawBoard(board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    # The X and O strings designate where to put the X and O images on the Window
    for i in range(3):
        for j in range(3):
            t = board[1 + i + 3*j]
            if t == 'X':
                pic = makePicture("blackx.jpg")
                pic.moveTo(100 + 200*i, 500 - 200*j)
                pic.draw(win)
            elif t == 'O':
                pic = makePicture("blacko.jpg")
                pic.moveTo(100 + 200*i, 500 - 200*j)
                pic.draw(win)

def to_num(move):
    (x,y) = move
    if (x, y) == (1,1):
        return 7
    if (x, y) == (1,2):
        return 8
    if (x, y) == (1,3):
        return 9
    if (x, y) == (2,1):
        return 4
    if (x, y) == (2,2):
        return 5
    if (x, y) == (2,3):
        return 6
    if (x, y) == (3,1):
        return 1
    if (x, y) == (3,2):
        return 2
    if (x, y) == (3,3):
        return 3

def to_xy(move):
    if move == 1:
        return (3, 1)
    if move == 2:
        return (3, 2)
    if move == 3:
        return (3, 3)
    if move == 4:
        return (2, 1)
    if move == 5:
        return (2, 2)
    if move == 6:
        return (2, 3)
    if move == 7:
        return (1, 1)
    if move == 8:
        return (1, 2)
    if move == 9:
        return (1, 3)

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    #print('Do you want to play again? (yes or no)')
    #return input('Do you want to play again? (yes or no)').lower().startswith('y')
    win.clear()
    if isWinner(theBoard, playerLetter):
        speak('Congratulations. You have won.')
        win.setBackground(Color('Green'))
        t = Text((300, 50), "YOU WIN!!! :)")
        t.draw(win)
    elif isWinner(theBoard, computerLetter):
        speak('You have lost.')
        win.setBackground(Color('Red'))
        t = Text((300, 50), "YOU LOSE!!! :(")
        t.draw(win)
    else:
        speak('It\'s a tie game.')
        win.setBackground(Color('Yellow'))
        t = Text((300, 50), "you tie!!! 0_o")
        t.draw(win)

    l = Line((300, 100), (300, 600))
    l.setWidth(10)
    l.draw(win)
    l = Line((0, 100), (600, 100))
    l.setWidth(10)
    l.draw(win)
    t = Text((150, 300), 'Play Again')
    t.draw(win)
    t = Text((450, 300), 'Quit')
    t.draw(win)

    speak('Do you want to play again, or quit?')

    x, y = getMouse()
    win.setBackground(Color('Gray'))
    if x < 300:
        return True
    else:
        win.clear()
        speak('Please close this window')
        t = Text((300, 300), "Please close this window...")
        t.draw(win)
        return False

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '

def getPlayerMove(board):
    # Let the player type in his move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        #print('What is your next move? (1-9)')
        #move = input('What is your next move? (1-9)')
        x, y = getMouse()
        x = x//200
        y = 2 - y//200
        move = str(int(1 + x + 3*y))

    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Check if the player could win on his next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


# The loop that runs the game
while True:
    # Reset the board
    win.clear()
    l = Line((200, 0), (200, 600))
    l.setWidth(10)
    l.draw(win)
    l = Line((400, 0), (400, 600))
    l.setWidth(10)
    l.draw(win)
    l = Line((0, 200), (600, 200))
    l.setWidth(10)
    l.draw(win)
    l = Line((0, 400), (600, 400))
    l.setWidth(10)
    l.draw(win)

    tgame = TicTacToe()
    state = tgame.initial
    theBoard = [' '] * 10
    playerLetter, computerLetter = 'X', 'O'
    turn = 'player'
    print('The player, X, always goes first')
    gameIsPlaying = True

    # Make this true if you want a chance to win...
    random_first_move = False

    while gameIsPlaying:
        if turn == 'player':
            # Player's turn.
            drawBoard(theBoard)

            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            drawBoard(theBoard)

            state = tgame.make_move(to_xy(move),state)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                #print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    #print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer's turn.
            if random_first_move:
                move = chooseRandomMoveFromList(theBoard, [1, 2, 3, 4, 5, 6, 7, 8, 9])
                while not isSpaceFree(theBoard, move):
                    move = chooseRandomMoveFromList(theBoard, [1, 2, 3, 4, 5, 6, 7, 8, 9])
                first = False
                move = to_xy(move)

            else:
                move = minimax_decision(state,tgame)
                
            drawBoard(theBoard)

            state = tgame.make_move(move,state)
            makeMove(theBoard, computerLetter, to_num(move))

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                #print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    #print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    t = Text((300, 10), "GAME OVER. CLICK TO CONTINUE")
    speak('Game over')
    t.draw(win)
    dummy, variable_that_doesnt_matter = getMouse() # Wait for click
    
    # Ask if they want to play again or quit
    if not playAgain():
        break
        