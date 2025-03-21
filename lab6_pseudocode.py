
Skip to content
Navigation Menu

    JoshuaF021

    cis129-projects

Code
Issues
Pull requests 1
Actions
Projects
Wiki
Security
Insights

    Settings

    cis129-projects

/
in
main

Indent mode
Indent size
Line wrap mode
Editing lab6_pseudocode.py file contents
Selection deleted
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
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


// The following code is Pseudocode
// Please convert the following code to Python Code and save as Lab6.py

// main module """                                
def main():
   #// Local variable for the total number of hot dogs needed.
   #Declare Integer total
   total = 0

   #input --------------------------------------
   #// Get the total number of hot dogs needed.
   total = getTotalHotDogs()

   #// Processing ----------------------------------
   #// Named constants for the package sizes
   #Constant Integer 
   DOGS = 10   #// Hot dogs in a package
   #Constant Integer 
   BUNS = 8    #// Hot dog buns in a package

   #// Local variables
   #Declare Integer 
   bunsLeft = 0  #// Left over hot dog buns
   #Declare Integer 
   minDogs = 0  #// Minimum packages of hot dogs
   #Declare Integer 
   minBuns = 0  #// Minimum packages of hot dog buns

   #// Calculate the number of left over hot dogs.
   #Set 
   dogsLeft = (DOGS - total MOD DOGS) MOD DOGS

   #// Calculate the minimum number of packages of hot dogs.
   #Set 
   minDogs = Math.ceil(total / DOGS) 

   #// Calculate the number of left over hot dog buns.
   #Set 
   bunsLeft = (BUNS - total MOD BUNS) MOD BUNS

   #// Calculate the minimum number of packages of hot dogs buns.
   #Set 
   minBuns = Math.ceil(total / BUNS) 

   #// Output ----------------------------------------
   #// Display the results.
   #Call 
   showResults(dogsLeft, minDogs, bunsLeft, minBuns)
#End Module

#// The getTotalHotDogs module gets the number of people
#// attending the cookout and the number of hot dogs each
#// person will be given, and stores the product in the
#// totalHotDogs reference variable.

#Function Integer 
def getTotalHotDogs():

   #// Local variables
   #Declare Integer 
   people = 0   #// Number of people attending
   #Declare Integer 
   hotDogs = 0 #// Hot dogs per person

   #// Get the number of people attending the cookout.
   people = input("Enter the number of people attending the cookout: ")
   #Input people

   #// Get the number of hot dogs each person will be given.
   hotDogs = input(" Enter the number of hot dogs for each person: ")
   #Input hotDogs

   #// Calculate the total number of hot dogs needed.
   total = people * hotDogs
   return total
#End Function

#// as an argument and calculates the minimum packages of hot
#// dogs and hot dog buns, the left over hot dogs and hot dog
#// buns, and displays the results.

#Module 
def ShowResults(dogsLeft, minDogs, bunsLeft, minBuns):

   #// Display the minimum packages of hot dogs needed.
   print("Minimum packages of hot dogs needed: ", minDogs)

   #// Display the minimum packages of buns needed.
   print("Minimum packages of hot dog buns needed: ", minBuns)

   #// Display the number of hot dogs left over.
   print("Hot dogs left over: ", dogsLeft)

   #// Display the number of hot dog buns left over.
   print("Hot dog buns left over: ", bunsLeft)
#End Module
