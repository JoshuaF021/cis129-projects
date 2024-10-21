"""Theater Seating Lab:

A dramatic theater has three seating sections, and it charges the following prices for tickets in each section:

section A seats cost $20 each, section B seats cost $15 each, and section C seats cost $10 each."""

main()
    A = 20
    B = 15
    C = 10

"""The theater has 300 seats in section A, 500 seats in section B, and 200 seats in section C."""

    Aseats = 300
    Bseats = 500
    Cseats = 200
    SENTINEL = -1
    newValue = 0
    counter = 0

print("Welcome to Josh's Theater Seating Lab!
      Section A seats cost ", A " each, section B seats cost ", B " each, and section C seats cost ", C " each.
      The theater has", Aseats " seats in section A, ", Bseats " seats in section B, and ", Cseats " seats in section C.")


"""Design a program that asks for the number of tickets sold in each section and then displays the amount of income generated from ticket sales. 
The program should validate the numbers that are entered for each section.
Make sure to generalize the process so that a theater can have any number of sections."""

Asold = 0
Bsold = 0
Csold = 0

Asold = input("How many tickes sold in section A?")
Bsold = input("How many tickes sold in section B?")
Csold = input("How many tickes sold in section C?")



newValue = getValidNumber()

while (newValue != SENTINEL)


    Here are some further clarifications about the Homework:
    A program that does not work, or crashes, will earn 0 points for the assignment.
    Write generalized routines. Do not have any hardcoded "A", "B", "C" outside of Main.
    Pass variables to generalized functions that return a value.
    ALL numbers in the problem statement MUST be stored in named constants. The section names should also be constants: A, B, C
    Design the program so it will be relatively easy to add a section D to the program by adding some constants and a few statements in main.
    Design the program so it will be easy to change the number of seats in each section or the cost of a seat in each section.
    Display a welcome message with all the constant values (not hardcoded)
    Give a subtotal for all purchases so far after each new purchase
    Display the overall total at the end of the program, and the number of seats and subtotals for each section


Submit completed Python code as a .py source file to D2L"""
