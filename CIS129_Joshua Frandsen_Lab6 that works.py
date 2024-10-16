#the code inside the functions seems to work perfectly (as you'll see if you run the code below)(I did have to define minDogs and minBuns as integers because they kept giving me floats for some reason)
#but trying to use the functions, somethimes it works and gives the right output
#sometimes it works and gives the wrong output (usually all zeroes or all zeroes except buns remaining)
#and sometimes it just gives me an error
# and I'm just going around in circles trying to fix the stupid thing

attendees = 0
hotDogs = 0
attendees = int(input("maximum attendees?"))
hotDogs = int(input("designated hot dogs per attendee?")) 
total = attendees * hotDogs

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

print("\nMinimum packages of hot dogs needed", int(minDogs))
print("Minimum packages of hot dog buns needed", int(minBuns))
print("Hot dogs remaining", int(dogsLeft))
print("Hot dog buns remaining", int(bunsLeft))
