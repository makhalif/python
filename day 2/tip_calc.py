print("Simple Tip calculator")
tip = int(input("what tip percent u wanna pay? 10, 12 or 15: \n"))

bill = int(input("what is your bill amount? \n"))

people = int(input("how many of you wanna contribute? \n"))
total_bill = bill * (tip/100) + bill

share = round(total_bill/people, 2)
print(f"Each person has to pay Kshs {share}")