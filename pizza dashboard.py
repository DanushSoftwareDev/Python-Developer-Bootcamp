#What size pizza dou you want????
#small pizza $15/$12
#medium pizza $20/$17
#large pizza $25/$21
# add extra toppings small pizza $2, +$3 for others
#extra cheese +$1
#stuffed crust +$4
#cheese burst +$6
print("Welcome to Pizza Deliveries!")
price = 0

# Getting the type of pizza
kind = input("Would you like a veggie pizza or a non-vegetarian? Enter 'v' for vegetarian and 'n' for non-vegetarian: ")
size = input("What size pizza do you want? Type 's' for small, 'm' for medium, or 'l' for large: ")

# Validating input
if (kind == "v" or kind == "n") and (size == "s" or size == "m" or size == "l"):
    # Determining base price
    if kind == "v":
        if size == "s":
            price = 12
        elif size == "m":
            price = 17
        elif size == "l":
            price = 21
    elif kind == "n":
        if size == "s":
            price = 15
        elif size == "m":
            price = 20
        elif size == "l":
            price = 25

    # Additional toppings
    toppings = input("Do you want extra toppings for your pizza? Type 'y' for Yes or 'n' for No: ")
    if toppings == "y":
        if size == "s":
            price += 2
        else:
            price += 3

    # Extra cheese
    extra_cheese = input("Do you want extra cheese? Type 'y' for Yes or 'n' for No: ")
    if extra_cheese == "y":
        price += 1

    # Stuffed crust
    stuffed_crust = input("Do you want a stuffed crust pizza? Type 'y' for Yes or 'n' for No: ")
    if stuffed_crust == "y":
        price += 4

    # Cheese burst
    cheese_burst = input("Would you like a cheese burst pizza? Type 'y' for Yes or 'n' for No: ")
    if cheese_burst == "y":
        price += 6

    # Final Bill
    print(f"Your total bill is ${price}. Your pizza will be delivered in 30 minutes. Thank you for choosing us!")
else:
    print("You entered an invalid input. Please try again.")
