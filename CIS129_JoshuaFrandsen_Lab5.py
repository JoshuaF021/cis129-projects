""" Joshua Frandsen
CIS 129 LAB 5

Write a program that will allow a grocery store to keep track of the total number of bottles collected for seven days.

The program will calculate the total number of bottles returned for the week and the amount paid out (the total returned times .10 cents). 

The output of the program should include the total number of bottles returned and the total paid out.  

The program will ask the user if they have more data to enter and will end the program if they do not. """

totalBottles = 0
#This variable will store the accumulated bottle values
counter = 1
#This variable will control the loop 
todayBottles = 0
#This variable will store the number of bottles returned on a day
totalPayout = 0
#This variable will store the calculated value of totalBottles times .10
keepGoing = "y"
#This variable will be used to run the program again

#while keepGoing == "y":
for counter in range(1,8):
    todayBottles = int(input(f"Enter number of bottles for day #{counter}:\n"))
    totalBottles += todayBottles
    todayBottles = 0

totalPayout = totalBottles * .1
print("The total number of bottles collected is",totalBottles)
print(f"The total paid out is ${totalPayout:.2f}")

#keepGoing = str(input("Do you want to enter another week’s worth of data? (Enter y or n):")