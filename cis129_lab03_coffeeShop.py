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

if coffees == 1:
  print(int(coffees),f"Coffee at $5: ${coffeetotal:.2f}")
else: print(int(coffees),f"Coffees at $5: ${coffeetotal:.2f}")
  
if muffins == 1:
  print(int(muffins),f"Muffin at $4: ${muffintotal:.2f}")
else: print(int(muffins),f"Muffins at $4 each: ${muffintotal:.2f}")
  
if teas == 1:
  print(int(teas),f"Tea at $3: ${teatotal:.2f}")
else: print(int(teas),f"Teas at $3 each: ${teatotal:.2f}")
  
if mochas == 1:
  print(int(mochas),f"Mocha at $7: ${mochatotal:.2f}")
else: print(int(mochas),f"Mochas at $7 each: ${mochatotal:.2f}")
print(f"6% tax: ${taxtotal:.2f}")
print("---------")
print(f"Total: ${grandtotal:.2f}")
print("***************************************\n")

#thank you message
print("""Thank you for vising Josh's online
coffee and muffin shop!
It was a pleasure serving you!
Enjoy your order 
and we hope to see you again soon! =)""")
