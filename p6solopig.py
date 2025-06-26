# Name: Christopher Lee
# ID: 10136117
import random

# roll variables
turnScore = 0
currentRoll = 0
neededPoints = 0
totalScore = 0

# this part does the assignment
while totalScore < 100:
    # p5 assignment
    if totalScore > 80:

        # calculate how many points we need to get
        neededPoints = 100 - totalScore
        print(f"Rolling for {neededPoints} points:")
        # then roll for the amount of points needed
        while turnScore < neededPoints:
            currentRoll = random.randint(1, 6)
            print(f"-rolled a {currentRoll}")
            if currentRoll == 1:
                print("you pig")
                turnScore = 0
                break
            else:
                turnScore += currentRoll

    else:
        # p4 of assignment
        print("Rolling for 20 points:")
        while turnScore < 20:
            currentRoll = random.randint(1, 6)
            print(f"-rolled a {currentRoll}")
            if currentRoll == 1:
                print("you pig")
                turnScore = 0
                break
            else:
                turnScore += currentRoll

    totalScore = totalScore + turnScore
    print(f"Turn Score: {turnScore}")
    print(f"Current Score: {totalScore}")
    print("Turn End")
    # don't forget to reset turn score
    turnScore = 0

print("A WINNER IS YOU")
