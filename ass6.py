units = int(input("Enter your electricity bill "))
bill = 0
if (units <= 100):
    print("Your electricity bill is", bill , "cents")
else:
    if (units < 200):
        units -= 100
        bill = units * 5
        print("Your electricity bill is", bill , "cents")
    else:
        bill += 500
        bill += (units - 200) * 10
        print("Your electricity bill is", bill , "cents")