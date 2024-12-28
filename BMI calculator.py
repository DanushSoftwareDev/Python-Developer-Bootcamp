height = float(input("What is your height in meters? \n"))
weight = float(input("What is your body weight in kgs? \n"))

# Calculate the bmi using weight and height.
bmi = round(weight / (height ** 2),2)
print("Your BMI is: " + str(bmi))