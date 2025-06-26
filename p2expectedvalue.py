# Name: Christopher Lee
# ID: 10136117
import random
import sys

# taking in command line argument and turning into integer
rollNum = sys.argv[1]
rollNum = float(rollNum)
rollNum = int(rollNum)
# roll variables
rollTot = 0
rollAvg = 0.00

# assignment
for i in range(1, rollNum + 1):
    rollTot = rollTot + random.randint(1, 6)

rollAvg = rollTot / rollNum

print("Rolling " + str(rollNum) + " times...")
print("Estimated expectation: " + str(rollAvg))
