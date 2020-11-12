height = int(input("Enter your height: "))

if height >= 150:
	print("You can buy the ticket now")
	age = int(input("How old are you? "))
	if age < 12:
		print("pay 120 shillings for the ticket")
	elif age <= 18:
		print("pay 150 shillings for the ticket")
	else:
		print("pay 200 shillings for the ticket")

else:
	print("Try when your a bit taller")