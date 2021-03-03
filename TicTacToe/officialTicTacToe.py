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

    play = False
    acceptableAnswers = ['Y', 'N', 'X', 'O', 1, 2]

    # Asking the user if they want to play
    while play == False:
        play = input("Do you want to play?: ").upper()
        if play not in acceptableAnswers:
            play = False

    return True


def show_board(boardList):
    # This function takes in the list that is keeping track of the moves
    # as the input and visualizes it as a 3x3 Tic Tac Toe board for the user

    # Adds space in between boards
    print("\n"*5)

    # Visualizes the board
    print(boardList[0], boardList[1], boardList[2])
    print(boardList[3], boardList[4], boardList[5])
    print(boardList[6], boardList[7], boardList[8])
