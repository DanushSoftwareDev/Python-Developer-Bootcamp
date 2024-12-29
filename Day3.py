#Using conditional statement -- if else
#Rollercoaster ticket
print("Welcome to the rollercoaster ")
height = int(input("What is your height in cms?\n"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    #Using nested if/else statements and elif statements
    age=int(input("How old are you? "))
    #ticket for children
    if age <= 12:
        bill = 5
        print("Children pay $5 for the ticket")
    #ticket for youth
    elif 18 >= age > 12:
        bill = 7
        print("Youth pay $7 for the ticket")
    #People with midlife crisis get a free ticket
    elif 55 >= age >= 45:
        bill = 0
        print("Everything is going to be okay. Have a free ride on us")
    #ticket for adults
    else:
        bill = 12
        print("Adults pay $12 for the ticket")
    want_photo=input("Do you want a photo ticket? type y for Yes or n for No. ")
    if want_photo == "y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry!, You're too short to ride a rollercoaster")

