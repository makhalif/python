print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L \n")
pepperoni = input("Do you want pepperoni? Y or N \n")
cheese = input("Do you want extra cheese? Y or N \n")
# small = 450
# medium = 600
# large = 750
# pepperoni = 50
# cheese = 100

# if size == "S" or size =="s":
# 	bill = small
# 	if add_pepperoni == "Y" or add_pepperoni == "y":
# 		bill = small + pepperoni
# 		if extra_cheese == "Y" or extra_cheese == "y":
# 			bill = small + pepperoni + cheese
# 	print(f"Your bill is {bill}")
# elif size == "M" or size == "m":
# 	bill = medium
# 	if add_pepperoni == "Y" or add_pepperoni == "y":
# 		bill = medium + pepperoni
# 		if extra_cheese == "Y" or extra_cheese == "y":
# 			bill = medium + pepperoni + cheese
# 	print(f"Your bill is {bill}")
# elif size == "L" or size == "l":
# 	bill = large
# 	if add_pepperoni == "Y" or add_pepperoni == "y":
# 		bill = large + pepperoni
# 		if extra_cheese == "Y" or extra_cheese == "y":
# 			bill = large + pepperoni + cheese
# 	print(f"Your bill is {bill}")
bill = 0

if size =='S' or size == 's':
	bill +=450
elif size == 'M' or size == 'm':
	bill +=600
elif size == 'L' or size == 'l':
	bill +=750

if pepperoni == 'y' or pepperoni == 'Y':
	if size == 's' or size =='S':
		bill +=50
	else:
		bill += 100
if cheese == 'Y' or cheese == 'y':
	bill +=100
print(f"Your final bill is Kshs {bill}")

