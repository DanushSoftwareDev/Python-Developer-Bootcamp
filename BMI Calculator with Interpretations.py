name = input("What is your name?\t")
print(f"Hello {name}!!")
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print(f"{name} you're underweight, your BMI is {bmi}")
elif bmi <= 25:
    print(f"{name} you're normal weight, your BMI is {bmi}")
elif bmi >= 25:
    print(f"{name} you're overweight, your BMI is {bmi}")
