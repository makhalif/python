


print("Check a year if it is a leap year or not")

year = int(input("Enter a year: "))

if year % 4 == 0:
	if year % 100 == 0:
		if year % 400:
			print ("a leap year")
		else:
			print("not a leap year")
	else:
		print("leap year")
	
else:
	print("not a leap year")