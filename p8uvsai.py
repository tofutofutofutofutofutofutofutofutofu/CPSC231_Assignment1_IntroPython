# Name: Christopher Lee
# ID: 10136117

import random


# function to roll to a number of points
# from p6
def rollTo(neededPoints):
    print(f"Rolling for {neededPoints} points:")
    turnScore = 0
    while neededPoints > turnScore:
        currentRoll = random.randint(1, 6)
        print(f"-rolled a {currentRoll}")
        if currentRoll == 1:
            print("player pigs")
            turnScore = 0
            break
        else:
            turnScore += currentRoll
    return turnScore


# calculate how many points the computer wants, change strat if you want to change strategy
strat = 20


def scoreCalculator(points):
    howMany = 100 - points
    if howMany > strat:
        return strat
    else:
        return howMany


# Variables
playerTurn = random.randint(1, 2)
player1Score = 0
player1TurnScore = 0
player2Score = 0
wantedPoints = 0
currentScore = 0
currentScoreBefore = 0

print("Welcome to PIG!")
# Looks at player turn and player score and does the rolling thing
while player1Score < 100 and player2Score < 100:
    currentScore = 0
    if playerTurn == 1:
        print(f"Computer Player's turn!")
        wantedPoints = scoreCalculator(player1Score)
        currentScore = rollTo(wantedPoints)
        player1Score += currentScore
        print(f"Turn Score: {currentScore}")
        print(f"Current score: {player1Score} vs {player2Score}")
        print()
        playerTurn += 1
# I feel like this was more painful than it should've been if I just rolled normally
    else:
        print(f"Your turn!")
        while True:
            playerChoice = input("Enter r to roll, h to hold or a number you want to roll to:").lower()
            if playerChoice == "r":
                currentScore += rollTo(2)
                if currentScore == currentScoreBefore:
                    break
                currentScoreBefore = currentScore
                print(f"Turn Score: {currentScore}")
            elif playerChoice == "h":
                player2Score += currentScore
                break
            else:
                currentScore = rollTo(int(playerChoice))
                player2Score += currentScore
                print(f"Turn Score: {currentScore}")
                break

        print(f"Current score: {player1Score} vs {player2Score}")
        print()
        input("Press Enter to Continue")
        playerTurn -= 1

# after someone won print prizes
if player1Score >= 100:
    print("Computer WINS!")
    # tfw computer has better luck than you
    print(f"Final score: {player1Score} vs {player2Score}")
else:
    print("YOU WIN!")
    print(f"Final score: {player1Score} vs {player2Score}")
