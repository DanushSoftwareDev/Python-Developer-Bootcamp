#Subscripting
#To fetch the last character of a string negative 1 is used as its index and we can count backwards
print("Hello"[-1])
print("Hello"[4])
print("Hello"[0])
print("Hello"[-5])

#Integer = Whole number
print(123+345)
#Large Integers which are often separated by a comma can be separated by an underscore
print(123_456_789)

#Float
print(3.14159)

#Boolean: Always starts with Capital T or Capital F
print(True)

#Checking Data type
print(type("hello"))
print(type(123))
print(type(12.34))
print(type(True))

#Type Casting
#Method 1
name="danush"
length=len(name)
print("The name has"+" "+str(length)+" "+"characters")

#Task 1
print("Number of letters in your name: "+ str(len(input("Enter your name\n"))))

#Mathematical Operations
# exponent **
# // To obtain an Integer instead of float
# % to obtain remainder
print(4%9)
print(3*3+3/3-3)

#Using round off
print(round(3/2))