# Name: Christopher Lee
# ID: 10136117
import random

# roll variables
turnScore = 0
currentRoll = 0
neededPoints = 0
totalScore = input("Enter the current total score as an integer: ")
totalScore = int(totalScore)

# this part does the assignment

if totalScore > 80:

    print("Rolling to win:")
    if totalScore >= 100:
        print("You already won!")
    # calculate how many points we need to get
    neededPoints = 100 - totalScore

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
