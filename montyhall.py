from __future__ import division
import random

winningDoor = 0
chosenDoor = 0
newChosenDoor = 0
counter = 0
iterations = input("Enter iterations to run: ")
timesNotSwapping = 0
timesSwapping = 0

while counter < iterations:
    winningDoor = random.randrange(0,3)
    chosenDoor = random.randrange(0,3)
    while True:
        openedDoor = random.randrange(0,3)
        if openedDoor != winningDoor and openedDoor != chosenDoor:
            break
    if counter >= (iterations/2): #Swapping algorithm
        while True:
            newChosenDoor = random.randrange(0,3)
            if newChosenDoor != openedDoor and newChosenDoor != chosenDoor:
                break
        if newChosenDoor == winningDoor:
            timesSwapping = timesSwapping + 1
    elif counter < (iterations/2): #Non-swapping algorithm
        if winningDoor == chosenDoor:
            timesNotSwapping = timesNotSwapping + 1
    counter = counter + 1

percentageSwapping = timesSwapping/(iterations/2) * 100
percentageNotSwapping = timesNotSwapping/(iterations/2) * 100
sum = percentageNotSwapping + percentageSwapping

print "The swapping method won %(number).2f%% of the time;" % {"number": percentageSwapping}
print "The non-swapping method won %(number).2f%% of the time;" % {"number": percentageNotSwapping}
print "The sum of both results is %(number).2f%%." % {"number": sum}