# Name: Christopher Lee
# ID: 10136117
import random
import sys

# taking in command line argument and turning into integer
turnNum = sys.argv[1]
turnNum = float(turnNum)
turnNum = int(turnNum)
# roll variables
turnCount = 0
currentRoll = 0
turnAvg = 0.00
# loop variable
i = 1

while i <= turnNum:
    currentRoll = random.randint(1, 6)
    # if you roll a 1, end turn and increment counter
    if currentRoll == 1:
        i = i + 1
    # anything else: add a turn and continue
    else:
        turnCount += 1

turnAvg = turnCount / turnNum

print("Playing " + str(turnNum) + " games...")
print("Estimated expected turns before pigging out: " + str(turnAvg))
