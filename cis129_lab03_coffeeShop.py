#This is a practice coffee shop program designed
#to request input from the user and output the 
#calculated total of the user's order including
#a 6% tax.

#Define cost of items
coffeeprice = 5.00
muffinprice = 4.00
teaprice = 3.00
mochaprice = 7.00
tax = .06

#Get input from the user
print("""***************************************
My Coffee and Muffin Shop\n""")
coffees = float(input("Number of coffees bought?\n"))
muffins = float(input("Number of muffins bought?\n"))
teas = float(input("Number of teas bought?\n"))
mochas = float(input("Number of mochas bought?\n"))
print("""***************************************""")

#calculate totals with tax of 6%
coffeetotal = coffeeprice * coffees
muffintotal = muffinprice * muffins
teatotal = teaprice * teas
mochatotal = mochaprice * mochas
taxtotal = tax * (coffeetotal + muffintotal + teatotal + mochatotal)
grandtotal = coffeetotal + muffintotal + teatotal + mochatotal + taxtotal

#print receipt
print("""\n***************************************
My Coffee and Muffin Shop Receipt""")
print(int(coffees),"Coffee at $5 each: $",coffeetotal)
print(int(muffins),"Muffins at $4 each: $",muffintotal)
print(int(teas),"Teas at $3 each: $",teatotal)
print(int(mochas),"Mochas at $7 each: $",mochatotal)
print("6% tax: $",taxtotal)
print("---------")
print("Total: $",grandtotal)
print("***************************************\n")

#thank you message
print("""Thank you for vising Josh's online
coffee and muffin shop!
It was a pleasure serving you!
Enjoy your order 
and we hope to see you again soon!""")
