# Name: Christopher Lee
# ID: 10136117
import random

# roll variables
turnScore = 0
currentRoll = 0

# this part does the assignment
while turnScore < 20:
    currentRoll = random.randint(1, 6)
    print("-rolled a " + str(currentRoll))
    if currentRoll == 1:
        print("you pig")
        turnScore = 0
        break
    else:
        turnScore += currentRoll

print("Current Score: " + str(turnScore))
print("Turn End")
