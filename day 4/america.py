import random 

seed_num = int(input("Enter seed number: "))
random.seed(seed_num)

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", 
					"Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", 
					"New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", 
					"Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", 
					"Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", 
					"California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", 
					"Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", 
					"Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# x = len(states_of_america) - 1

# random_state = random.randint(0, x)
random_state = random.choice(states_of_america)

print(random_state)

# print(states_of_america)



