""" Joshua Frandsen
CIS 129 LAB 5

Write a program that will allow a grocery store to keep track of the total number of bottles collected for seven days.

The program will calculate the total number of bottles returned for the week and the amount paid out (the total returned times .10 cents). 

The output of the program should include the total number of bottles returned and the total paid out.  

The program will ask the user if they have more data to enter and will end the program if they do not. """

#This variable will store the accumulated bottle values
totalBottles = 0
#This variable will control the loop 
counter = 1
#This variable will store the number of bottles returned on a day
todayBottles = 0
#This variable will store the calculated value of totalBottles times .10
totalPayout = 0
#This variable will be used to run the program again
keepGoing = "y"

# loop to repeat program each time user inputs y at end of program
while keepGoing == "y":
    #input loop to collect number of bottles each day for 7 days and add all 7 inputs to total for the week
    for counter in range(1,8):
        todayBottles = int(input(f"Enter number of bottles for day #{counter}: "))
        totalBottles += todayBottles
        #reset's variable for next loop
        todayBottles = 0
    # calculates payout based on total bottles collected for the week
    totalPayout = totalBottles * .1

    #Prints total bottles collected for the week and  total payout for the week
    print("\nThe total number of bottles collected is",totalBottles)
    print(f"The total paid out is ${totalPayout:.2f}")

    #resets variable for next loop
    totalBottles = 0

    # asks user if they want to run the program again and input becomes variable's new value
    keepGoing = str(input("\nDo you want to enter another week’s worth of data?\n(Enter y or n): "))
    
