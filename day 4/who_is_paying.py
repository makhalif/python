import random 

seed_num = int(input("Enter your seed number: "))
random.seed(seed_num)

names = input("Enter the names: ")
friends_name = names.split(",")
# list size
# x = len(friends_name) - 1
#pick a random index of the list
# random_name = random.randint(0,x)
# print(friends_name[random_name])
random_name = random.choice(friends_name) #replace the three lines of code above

print(random_name)

