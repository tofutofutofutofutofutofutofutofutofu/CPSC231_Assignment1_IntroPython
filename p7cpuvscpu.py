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
            print("you pig")
            turnScore = 0
            break
        else:
            turnScore += currentRoll
    print(f"Turn Score: {turnScore}")
    return turnScore


# calculate how many points the computer wants, change strat if you want to change strategy
def scoreCalculator(points):
    howMany = 100 - points
    strat = 20
    if howMany > strat:
        return strat
    else:
        return howMany


# Variables
playerTurn = random.randint(1, 2)
player1Score = 0
player2Score = 0
wantedPoints = 0

# Looks at player turn and player score and does the rolling thing
while player1Score < 100 and player2Score < 100:

    if playerTurn == 1:
        print(f"Player {playerTurn}'s turn!")
        wantedPoints = scoreCalculator(player1Score)
        player1Score += rollTo(wantedPoints)
        print(f"Current score: {player1Score} vs {player2Score}")
        print()
        playerTurn += 1

    else:
        print(f"Player {playerTurn}'s turn!")
        wantedPoints = scoreCalculator(player2Score)
        player2Score += rollTo(wantedPoints)
        print(f"Current score: {player1Score} vs {player2Score}")
        print()
        playerTurn -= 1

# after someone won print prizes
if player1Score >= 100:
    print("Player One wins!")
    print(f"Final score: {player1Score} vs {player2Score}")
else:
    print("Player Two wins!")
    print(f"Final score: {player1Score} vs {player2Score}")
