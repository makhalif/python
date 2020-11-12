print("Love calculator")

nam1 = input("Enter your name: ")
nam2 = input("Enter their name: ")

names = nam1+nam2
name = names.lower()

# print(name)
t = name.count("t") 
r = name.count("r") 
u = name.count("u") 
e = name.count("e") 
true = t + r + u + e

l = name.count("l")  
o = name.count("o") 
v = name.count("v")
e = name.count("e") 
love = l + o + v + e

score = int(str(true) + str(love))

if score <=25:
	print(f"Look for another one my friend, your compatibility score is {score}%")
elif score >=26 and score<=49:
	print(f"Your compatibility is below average, work on it please, your compatibility score is {score}%")
elif score >=50 and score<=70:
	print(f"Good compatibility, keep the love burning. your compatibility score is {score}%")
else:
	print(f"wow! where did you find each other. your compatibility score is {score}%")


