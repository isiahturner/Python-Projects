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
    play = 0
