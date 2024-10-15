"""Assume that hot dogs come in packages of 10, and hot dog buns come in packages of 8. Design a modular program that calculates the number of packages of hot dogs and the number of packages of hot dog buns needed for a cookout, with the minimum amount of leftovers. The program should ask the user for the number of people attending the cookout, and the number of hot dogs each person will be given. The program should display the following:

    The minimum number of packages of hot dogs required.
    The minimum number of packages of buns required
    The number of hot dogs that will be left over
    The number of buns that will be left over"""


#Program Start
Initialize totalHotDogs variable
Call getTotalHotDogs function and assign it to totalHotDogs
Call showResults, passing totalHotDogs as an argument

Function getTotalHotDogs:
  Initialize attendees
  Initialize hotDogs
  Ask user for maximum attendees and assign to attendees
  Ask user for designated hot dogs per attendee and assign to hotDogs
  Total = attendees * hotDogs
  Return total

Function showResults:
  Initialize constant DOGS as 10
  Initialize constant BUNS as 8
  Initialize dogsLeft 
  Initialize bunsLeft
  Initialize minDogs 
  Initialize minBuns 
  Set dogsLeft as result of equation using DOGS, total and dogsLeft
  Set minDogs as result of equation using total, DOGS and dogsLeft
  Set bunsLeft as result of equation using BUNS, total and bunsLeft
  Set minBuns as result of equation using total, BUNS and bunsLeft
  Display "Minimum packages of hot dogs needed" along with the value of minDogs
  Display "Minimum packages of hot dog buns needed" along with the value of minBuns
  Display "Hot dogs remaining" along with the value of dogsLeft
  Display "Hot dog buns remaining" along with the value of bunsLeft

End of Program
