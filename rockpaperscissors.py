def rockpaperscissors(userInput1, userInput2):
    if ((userInput1 == "paper") & (userInput2 == "rock")):
        print("paper  won")
    elif ( ( userInput1 == "rock") & (userInput2 == "scissors")):
        print("rock  won")
    elif (( userInput1 == "scissors") & (userInput2 == "paper")):
        print("scissors  won")
    elif (userInput1 == userInput2):
        print("draw")
    elif (( userInput2 == "paper") & (userInput1 == "rock")):
        print("paper  won")
    elif ((userInput2 == "rock") & (userInput1 == "scissors")):
        print("rock  won")
    elif (( userInput2 == "scissors") & (userInput1 == "paper")):
        print("scissors  won")


rockpaperscissors("rock", "paper")
rockpaperscissors("paper", "rock")
rockpaperscissors("scissors", "rock")
rockpaperscissors("rock", "scissors")