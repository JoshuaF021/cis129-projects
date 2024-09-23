#Define cost of items
coffeeprice = 5.00
muffinprice = 4.00
tax = .06

#Get input from the customer
print("""***************************************
My Coffee and Muffin Shop""")
coffees = float(input("Number of coffees bought?\n"))
muffins = float(input("Number of muffins bought?\n"))
print("""***************************************""")

#calculate totals with tax of 6%
coffeetotal = coffeeprice * coffees
muffintotal = muffinprice * muffins
taxtotal = tax * (coffeetotal + muffintotal)
grandtotal = coffeetotal + muffintotal + taxtotal

#print receipt
print("""\n***************************************
My Coffee and Muffin Shop Receipt""")
print(int(coffees),"Coffee at $5 each: $",coffeetotal)
print(int(muffins),"Muffins at $4 each: $",muffintotal)
print("6% tax: $",taxtotal)
print("---------")
print("Total: $",grandtotal)
print("***************************************")
