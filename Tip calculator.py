print("Welcome to the Tip Calculator")
bill=float(input("What was the total bill?\n"))
tip=int(input("How much tip would you like to give: 10%, 12%, 15%, 18%, 20%\n"))
num_of_people=int(input("How many people to split the bill?\n"))
total=(bill+(bill*(tip/100)))/num_of_people
print(f"Each person should pay: {round(total,2)}")
