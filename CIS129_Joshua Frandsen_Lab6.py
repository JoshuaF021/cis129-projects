"""Joshua Frandsen
    CIS129 LAB 6
    10/15/2024"""

"""Assume that hot dogs come in packages of 10, and hot dog buns come in packages of 8. 
Design a modular program that calculates the number of packages of hot dogs and the number of packages of hot dog buns needed for a cookout, with the minimum amount of leftovers. 
The program should ask the user for the number of people attending the cookout, and the number of hot dogs each person will be given. The program should display the following:

    The minimum number of packages of hot dogs required.
    The minimum number of packages of buns required
    The number of hot dogs that will be left over
    The number of buns that will be left over"""


#Program Start
#Set variables
totalHotDogs = 0

totalHotDogs = getTotalHotDogs() 
showResults(totalHotDogs)

def getTotalHotDogs(totalHotDogs):
    attendees = 0
    hotDogs = 0
    attendees = int(input("maximum attendees?"))
    hotDogs = int(input("designated hot dogs per attendee?")) 
    total = attendees * hotDogs
    return total

def showResults(totalHotDogs):
    DOGS = 10
    BUNS = 8
    dogsLeft = 0 
    bunsLeft = 0
    minDogs = 0
    minBuns = 0 
    #Set dogsLeft as result of equation using DOGS, total and dogsLeft
    dogsLeft = (DOGS - total % DOGS) % DOGS
    #Set minDogs as result of equation using total, DOGS and dogsLeft
    minDogs = (total / DOGS) + (0 ** (0 ** dogsLeft))
    #Set bunsLeft as result of equation using BUNS, total and bunsLeft
    bunsLeft = (BUNS - total % BUNS) % BUNS
    #Set minBuns as result of equation using total, BUNS and bunsLeft
    minBuns = (total / BUNS) + (0 ** (0 ** bunsLeft))

    print("\nMinimum packages of hot dogs needed", minDogs)
    print("Minimum packages of hot dog buns needed", minBuns)
    print("Hot dogs remaining", int(dogsLeft))
    print("Hot dog buns remaining", int(bunsLeft))




#End of Program
