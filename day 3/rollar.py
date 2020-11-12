height = int(input("Enter your height: "))
bill = 0

if height >= 150:
	print("You can buy the ticket now")
	age = int(input("How old are you? "))
	if age <= 12:
		bill = 120
		print("child ticket is 120 shillings")
	elif age <= 18:
		bill = 150
		print("teenage ticket is 150 shillings")
	else:
		bill = 200
		print("adult ticket is 200 shillings")
	photo = input("Do you want a photo taken? Y or N :\n")

	if photo == "Y" or photo == 'y':
		bill +=50
	print(f"the final bill is {bill}")

else:
	print("Try when your a bit taller")