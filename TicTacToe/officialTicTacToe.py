# My rendition of Tic Tac Toe. The game is designed for two
# users on the same computer and the users will get to decide
# who goes first and which letter they want to use during their
# turn. Then when a winner is decided or the game ends in a
# draw, the users will have the opportunity to continue playing
# the game or end the game if they want to.

# Defining functions

def game_on():
    # This is the function that asks if the users want to play
    # the first time and any point after that. Takes in no
    # arguments and will have an output True/False to set the
    # while loop conditional to play the game

    loopCheck = False
    acceptableAnswers = ['Y', 'N']

    # Asking the user if they want to play
    while loopCheck == False:
        playCheck = input("Do you want to play?: ").upper()
        if playCheck in acceptableAnswers and playCheck == 'Y':
            play = True
            loopCheck = True
        elif playCheck in acceptableAnswers and playCheck == 'N':
            play = False
            loopCheck = True
        else:
            loopCheck = False

        if play == False:
            print("\n")
            print("MAYBE NEXT TIME!")
            print("\n")

    return play


def showBoard(boardList):
    # This function takes in the list that is keeping track of the moves
    # as the input and visualizes it as a 3x3 Tic Tac Toe board for the user

    # Adds space in between boards
    print("\n")

    # Visualizes the board
    print(boardList[0], boardList[1], boardList[2])
    print(boardList[3], boardList[4], boardList[5])
    print(boardList[6], boardList[7], boardList[8])

    print("\n")


def turnDecider(emptyDict):
    # The point of this function is to ask for the player's input
    # (which turn they want and which letter they want).
    # The key will be if they want to go first or second and
    # the value will be their assigned letter. This dictionary
    # will be used later to replace values in the board list

    check = False
    answers = ['X', 'O', 1, 2]

    while check == False:
        playerTurn = int(input("Which turn would you like to go (1 or 2)?: "))
        playerLetter = input(
            "Which letter do you want to use (X or O)?: ").upper()
        if playerTurn not in answers and playerLetter not in answers:
            check = False
        else:
            check = True

    if playerTurn == 1 and playerLetter == 'X':
        emptyDict[0] = 'X'
        emptyDict[1] = 'O'
    elif playerTurn == 2 and playerLetter == 'X':
        emptyDict[0] = 'O'
        emptyDict[1] = 'X'
    elif playerTurn == 1 and playerLetter == 'O':
        emptyDict[0] = 'O'
        emptyDict[1] = 'X'
    elif playerTurn == 2 and playerLetter == 'O':
        emptyDict[0] = 'X'
        emptyDict[1] = 'O'

    return emptyDict


def playerMove(usedMoves, boardList, playerDict, counter):
    # This function will take in a list of all of the moves
    # previously used and a list of the board as the parameters.
    # The function will ask for player input for their move,
    # update the board and update the used moves list. This
    # function will return the updated lists. COUNTER STARTS AT
    # 1!

    check = False

    while check == False:
        # Checking if they input is valid
        move = input("Where do you want to go for your move (Choose 1-9)?: ")
        if move.isdigit() and int(move) in range(1, 10):
            move = int(move)
            # Checking if the move has already been played. Force loop again
            # or update the lists
            if move in usedMoves:
                print("That spot is taken! Try again.")

            else:
                usedMoves.append(move)
                boardList[move-1] = playerDict[(counter + 1) % 2]
                print("\n"*3)
                print("Now it is " +
                      playerDict[counter % 2] + "'s turn!")
                check = True

    return usedMoves, boardList


def winConCheck(boardList, counter):
    if (boardList[0] == 'X' and boardList[1] == 'X' and boardList[2] == 'X')\
            or\
            (boardList[0] == 'O' and boardList[1] == 'O' and boardList[2] == 'O'):
        print("\n")
        print("GAME OVER")
        return "gg"
    elif (boardList[0] == 'X' and boardList[3] == 'X' and boardList[6] == 'X')\
            or\
            (boardList[0] == 'O' and boardList[3] == 'O' and boardList[6] == 'O'):
        print("\n")
        print("GAME OVER")
        return "gg"
    elif (boardList[0] == 'X' and boardList[4] == 'X' and boardList[8] == 'X')\
            or\
            (boardList[0] == 'O' and boardList[4] == 'O' and boardList[8] == 'O'):
        print("\n")
        print("GAME OVER")
        return "gg"
    elif (boardList[2] == 'X' and boardList[4] == 'X' and boardList[6] == 'X')\
            or\
            (boardList[2] == 'O' and boardList[4] == 'O' and boardList[6] == 'O'):
        print("\n")
        print("GAME OVER")
        return "gg"
    elif (boardList[2] == 'X' and boardList[5] == 'X' and boardList[8] == 'X')\
            or\
            (boardList[2] == 'O' and boardList[5] == 'O' and boardList[8] == 'O'):
        print("\n")
        print("GAME OVER")
        return "gg"
    elif (boardList[6] == 'X' and boardList[7] == 'X' and boardList[8] == 'X')\
            or\
            (boardList[6] == 'O' and boardList[7] == 'O' and boardList[8] == 'O'):
        print("\n")
        print("GAME OVER")
        return "gg"
    elif (boardList[1] == 'X' and boardList[4] == 'X' and boardList[7] == 'X')\
            or\
            (boardList[1] == 'O' and boardList[4] == 'O' and boardList[7] == 'O'):
        print("\n")
        print("GAME OVER")
        return "gg"
    elif (boardList[3] == 'X' and boardList[4] == 'X' and boardList[5] == 'X')\
            or\
            (boardList[3] == 'O' and boardList[4] == 'O' and boardList[5] == 'O'):
        print("\n")
        print("GAME OVER")
        return "gg"
    elif '1' not in boardList and counter >= 9:
        print("\n")
        print("It's a tie!")
        return "gg"
    else:
        return "pass"

# Playing the game using a while loop and the functions
# If the WinCon function results in a win/tie, it's output will be used in an if statement to give the player
# an option to continue playing or to end the game


start = game_on()

# Making the game playable
while start == True:
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    usedMoves = []
    counter = 1
    whosFirst = {}
    whosFirst = turnDecider(whosFirst)
    while counter < 10:
        showBoard(board)
        playerMove(usedMoves, board, whosFirst, counter)
        winner = winConCheck(board, counter)
        counter += 1
        if winner == "gg":
            showBoard(board)
            start = game_on()
            counter = 10


#board = ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'O']
#playerDict = {0: 'X', 1: 'O'}
# showBoard(board)
#print(winConCheck(board, playerDict, 9))


# Checking to see whether playerMove function worked properly
# board = ['X', '2', '3', '4', '5', '6', '7', '8', '9']
# usedMoves = [1]
# counter = 3
# playerDict = {0: 'X', 1: 'O'}
# usedMoves, board = playerMove(usedMoves, board, playerDict, counter)
# print(usedMoves)
# print(board)
