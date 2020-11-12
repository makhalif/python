print("Simple BMI calculator\n")
print("--------------------")

weight = int(input("Enter your weight in kg: \n"))
height = float(input("Enter height in m: \n"))
bmi = round(weight/height **2, 1)

print(f"Your BMI is {bmi}")