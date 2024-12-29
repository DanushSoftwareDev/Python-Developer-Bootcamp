#Even numbers when divided by 2 leaves no remainder
number=int(input("Enter a whole number\n"))
# '/' is used to find the quotient and '%' is used to find the remainder
if number % 2 == 0:
    print("The number that you entered is an even number")
else:
    print("The number that you entered is an odd number")