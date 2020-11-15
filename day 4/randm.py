import random 

# random_integer = random.randint(1, 20)
# print(random_integer)

# random_float = random.random()
# print(random_float)

love_score = random.randint(1, 100)
if love_score <=25:
	print(f"Your love score is {love_score}%  and your compatibility is bellow average")
elif love_score >= 26 and love_score<=50:
	print(f"Your love score is {love_score}%, your compatibility is good")
else:
	print(f"Your love score is {love_score}%, perfect compatibility")