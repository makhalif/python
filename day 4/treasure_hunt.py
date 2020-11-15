row1 = ["🤠", "🤠", "🤠"]
row2 = ["🤠", "🤠", "🤠"]
row3 = ["🤠", "🤠", "🤠"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ") #the input is a stringlets say 23 is the input

horizontal = int(position[0]) #the first value of the input is saved here,2 is saved here
vertical = int(position[1])  #the second value of the input is saved here and 3 is saved here

selected_row = map[vertical-1]
#print(selected_row)
selected_row[horizontal-1] = " X "

print(f"{row1}\n{row2}\n{row3}")