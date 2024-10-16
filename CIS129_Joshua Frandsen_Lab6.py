"""Joshua Frandsen
    CIS129 LAB 6
    10/15/2024"""

#Program Start


#calls to Functions
#getTotalHotDogs(totalHotDogs) 
#showResults(totalHotDogs)

def main():
    #Set variable
    totalHotDogs = 0
    #call functions
    totalHotDogs = getTotalHotDogs()
    showResults(totalHotDogs)


#define function that asks for number of attendees and dogs per attendee, calculates the total and sets that value to the variable total
def getTotalHotDogs():
    #sets variables
    attendees = 0
    hotDogs = 0
    #asks for input from user
    attendees = int(input("maximum attendees?"))
    hotDogs = int(input("designated hot dogs per attendee?"))
    #calculate and return total
    total = attendees * hotDogs
    return total

# define function to calculate and print out number of hot dog packs needed, bun packs needed, remaining dogs and remaining buns, based on total from getTotalHotDogs function above
def showResults(total):
    #set constants and variables
    DOGS = 10
    BUNS = 8
    dogsLeft = 0 
    bunsLeft = 0
    minDogs = 0
    minBuns = 0 
    #Set dogsLeft as result of equation using DOGS, total and dogsLeft
    dogsLeft = (DOGS - total % DOGS) % DOGS
    #Set minDogs as result of equation using total, DOGS and dogsLeft
    int(minDogs) == (total / DOGS) + (0 ** (0 ** dogsLeft))
    #Set bunsLeft as result of equation using BUNS, total and bunsLeft
    bunsLeft = (BUNS - total % BUNS) % BUNS
    #Set minBuns as result of equation using total, BUNS and bunsLeft
    int(minBuns) == (total / BUNS) + (0 ** (0 ** bunsLeft))

    #print out number of hot dog packs needed, bun packs needed, remaining dogs and remaining buns
    print("\nMinimum packages of hot dogs needed", int(minDogs))
    print("Minimum packages of hot dog buns needed", int(minBuns))
    print("Hot dogs remaining", int(dogsLeft))
    print("Hot dog buns remaining", int(bunsLeft))

main()
#End of Program
