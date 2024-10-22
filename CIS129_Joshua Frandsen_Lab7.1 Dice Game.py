""" Joshua Frandsen
CIS129 Dice Game Lab 7
10/21/2024"""

# add libraries needed
import random

# the main function
def main():
    print()
    # initialize variables
    endProgram = 'no'
    playerOne = 'NO NAME'
    playerTwo = 'NO NAME'
    # call to inputNames
    playerOne, playerTwo = inputNames(playerOne, playerTwo)
    # while loop to run program again
    while endProgram == 'no':
          # populate variables
          winnersName = 'NO NAME'
          p1number = 0
          p2number = 0
    

# call to displayInfo
def displayInfo(winnerName):
    endProgram = input('Do you want to end program? (yes/no): ')

#this function gets the players names
def inputNames(playerOne, playerTwo):
    playerOne = input("Enter First Player Name:")
    playerTwo = input("Enter Second Player Name:")
    return playerOne, playerTwo

#this function will get the random values
def rollDice(p1number, p2number, playerOne, playerTwo, winnerName):
    p1number = random.randint(1, 6)
    p2number = random.randint(1, 6)

    if p1number == p2number:
        winnerName = 'TIE'
    elif p1number > p2number:
            winnerName == playerOne
    else: winnerName == playerTwo
    return winnerName

# call to rollDice
winnerName = rollDice(p1number, p2number, playerOne, playerTwo, winnerName)

#this function displays the winner
displayInfo(winnerName)
print(winnerName)
# calls main
main()
