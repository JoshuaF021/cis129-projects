# Module 4 Lab 4
# Joshua Frandsen
# 1st of Oct 2024
# Program purpose: to determine the amount (if any)
# of the store bonus and employee bonus
# based on sales goals
# and display said amounts.

# The main function
def main():
    monthlySales = getSales() #call to get sales
    salesIncrease = getIncrease() #call to get sales increase
    storeAmount = storeBonus(monthlySales) #call to get the store bonus
    empAmount = empBonus(salesIncrease) #call to get the employee bonus
    printBonus(storeAmount, empAmount) #call to print amounts
  
# This function gets the monthly sales
def getSales():
    monthlySales = float(input("Enter the monthly sales $"))
    return monthlySales

# This function determines the storeAmount bonus
def calcStoreBonus(monthlySales):
    if monthlySales >= 110000:
          storeAmount = 6000
    elif monthlySales >= 100000:
          storeAmount = 5000
    elif monthlySales >= 90000:
          storeAmount = 4000
    elif monthlySales >= 80000:
          storeAmount = 3000
    else: storeAmount = 0
    return storeAmount

# This function gets the percent of increase in sales
def getIncrease():
    salesIncrease = float(input("Enter percent of sales increase without % sign aka 50 instead of 50%"))
    salesIncrease = salesIncrease / 100
    return salesIncrease

# This function determines the empAmount bonus
def calcEmpBonus(salesIncrease):
    if salesIncrease >= .05:
        empAmount = 75
    elif salesIncrease >= .04:
        empAmount = 50
    elif salesIncrease >= .03:
        empAmount = 40
    else:
        empAmount = 0
    return
  
# This function prints the bonus information
def printBonus(storeAmount,empAmount):
    print("The store bonus amount is $",storeAmount)
    print("The employee bonus amount is $",empAmount)
    if (storeAmount == 6000 ) and (empAmount == 75):
        print('Congrats! You have reached the highest bonus amounts\
               possible!')
    
# calls main
main()
