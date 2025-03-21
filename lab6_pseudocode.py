"""
Hotdog Cookout Lab:
Students will be provided the Pseudocode, then they are to create this in Python.

Hot Dog Cookout Calculator

Assume that hot dogs come in packages of 10, and hot dog buns come in packages of 8. 
Design a modular program that calculates the number of packages of hot dogs and the number of 
packages of hot dog buns needed for a cookout, with the minimum amount of leftovers. 
The program should ask the user for the number of people attending the cookout, and the 
number of hot dogs each person will be given. The program should display the following:

1. The minimum number of packages of hot dogs required.
2. The minimum number of packages of buns required
3. The number of hot dogs that will be left over
4. The number of buns that will be left over

Programming Exercise (Hotdog Cookout Calculator)
"""

// The following code is Pseudocode
// Please convert the following code to Python Code and save as Lab6.py

// main module                                 
Module main()
   // Local variable for the total number of hot dogs needed.
   Declare Integer total

   // Input --------------------------------------
   // Get the total number of hot dogs needed.
   total = getTotalHotDogs()

   // Processing ----------------------------------
   // Named constants for the package sizes
   Constant Integer DOGS = 10   // Hot dogs in a package
   Constant Integer BUNS = 8    // Hot dog buns in a package

   // Local variables
   Declare Integer dogsLeft  // Left over hot dogs
   Declare Integer bunsLeft  // Left over hot dog buns
   Declare Integer minDogs   // Minimum packages of hot dogs
   Declare Integer minBuns   // Minimum packages of hot dog buns

   // Calculate the number of left over hot dogs.
   Set dogsLeft = (DOGS - total MOD DOGS) MOD DOGS

   // Calculate the minimum number of packages of hot dogs.
   Set minDogs = Math.ceil(total / DOGS) 

   // Calculate the number of left over hot dog buns.
   Set bunsLeft = (BUNS - total MOD BUNS) MOD BUNS

   // Calculate the minimum number of packages of hot dogs buns.
   Set minBuns = Math.ceil(total / BUNS) 

   // Output ----------------------------------------
   // Display the results.
   Call showResults(dogsLeft, minDogs, bunsLeft, minBuns)
End Module

// The getTotalHotDogs module gets the number of people
// attending the cookout and the number of hot dogs each
// person will be given, and stores the product in the
// totalHotDogs reference variable.

Function Integer getTotalHotDogs()

   // Local variables
   Declare Integer people   // Number of people attending
   Declare Integer hotDogs  // Hot dogs per person

   // Get the number of people attending the cookout.
   Display "Enter the number of people attending the cookout: "
   Input people

   // Get the number of hot dogs each person will be given.
   Display " Enter the number of hot dogs for each person: "
   Input hotDogs

   // Calculate the total number of hot dogs needed.
   total = people * hotDogs
   return total
End Function

// The showResults module accepts the total number of hot dogs
// as an argument and calculates the minimum packages of hot
// dogs and hot dog buns, the left over hot dogs and hot dog
// buns, and displays the results.

Module ShowResults(Integer dogsLeft, Integer minDogs, 
                   Integer bunsLeft, Integer minBuns)

   // Display the minimum packages of hot dogs needed.
   Display "Minimum packages of hot dogs needed: ", minDogs

   // Display the minimum packages of buns needed.
   Display "Minimum packages of hot dog buns needed: ", minBuns

   // Display the number of hot dogs left over.
   Display "Hot dogs left over: ", dogsLeft

   // Display the number of hot dog buns left over.
   Display "Hot dog buns left over: ", bunsLeft
End Module

