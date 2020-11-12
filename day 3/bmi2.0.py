print("BMI Calculator 2.0\n")
height = float(input("Enter your height in m: "))
weight = int(input("Enter your weight in kg: "))

bmi = round(weight/height ** 2, 1)

print(f"Your BMI is {bmi}")

if bmi <18.5:
	print("You are under weight, eat well please")
elif bmi<=25:
	print("Your BMI is normal, maintain it please")
elif bmi<=35:
	print("you are obese, try to loss some weight")
else:
	print("you are extremely obese, go fuck yourself.")