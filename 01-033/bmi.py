height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
BMI = weight / (height/100)**2
print(f"You BMI is {BMI}")

if BMI <= 18.4:
    print(f" you bim is {BMI}, You are underweight.")
elif BMI <= 24.9:
    print(f"you bim is {BMI},You are healthy.")
elif BMI <= 29.9:
    print(f"you bim is {BMI},,You are over weight.")
elif BMI <= 34.9:
    print(f"you bim is {BMI},,You are severely over weight.")
elif BMI <= 39.9:
    print(f"you bim is {BMI},,You are obese.")
else:
    print(f"you bim is {BMI},,You are severely obese.")