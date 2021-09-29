import random as random
import time


def play():
    player = input("Choose between 1 = Rock, 2 = Paper, 3 = Scissors")
    playerNumber = int(player)
    if playerNumber > 3:
        print("Your Number is too big")
    computerNumber = random.randrange(1,3)

    if computerNumber == 1:
        computerGuess = "Rock"
    elif computerNumber == 2:
        computerGuess = "Paper"
    else:
        computerGuess = "Scissors"
    print("Computer chose "+computerGuess)

    time.sleep(1.5)

    if computerNumber == 1 and playerNumber == 1:
        print("Draw")
    elif computerNumber == 1 and playerNumber == 2:
        print("Player Wins")
    elif computerNumber == 1 and playerNumber == 3:
        print("Computer Wins")
    elif computerNumber == 2 and playerNumber == 1:
        print("Computer Wins")
    elif computerNumber == 2 and playerNumber == 2:
        print("Draw")
    elif computerNumber == 2 and playerNumber == 3:
        print("Player Wins")
    elif computerNumber == 3 and playerNumber == 1:
        print("Computer Wins")
    elif computerNumber == 3 and playerNumber == 2:
        print("Computer Wins")
    elif computerNumber == 3 and playerNumber == 3:
        print("Draw")


play()




