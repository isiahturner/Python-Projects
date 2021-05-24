# Initializing Variables needed for the game: turn counter, board
counter = 0
board = [1, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def game_on():
    play = input("Do you want to play again (Y/N)?: ")
    if play == "Y":
        return "play"
    elif play == "N":
        return "no play"


play = game_on()
print(game_on)

while play == "play":
    print("happy")
    counter += 1

    if counter > 3:
        play = game_on()
    else:
        pass
