play = 1
while play == 1:
    counter = 0
    game_continued = "on"
    while game_continued == "on":
        counter += 1
        print(counter)
        if counter > 2:
            game_continued = "off"
        else:
            pass

    print(counter)
    print(" ")
    play = 0


board = ['X', '2', '3', '4', '5', '6', '7', '8', '9']
print(board[0], board[1], board[2])
