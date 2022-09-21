amount = int(input("amount: "))
currency = input("(N) or (D): ")
if currency == "D":
    convert = amount * 700
    print("amount in N: " + str(convert))
else:
    convert = amount / 700
    print("amount in D: " + str(convert))

