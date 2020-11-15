import random

my_seed = int(input("Create a seed number: "))
random.seed(my_seed)

random_integer = random.randint(0,1) 

if random_integer == 1:
	print("Head")
else:
	print("Tail")