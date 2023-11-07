Students = 175
grpSize = 24

grpTotal = int(Students / grpSize)
grpSmall = Students - (grpTotal * grpSize)

print(f"The total amount of students that are in full groups are {grpTotal}, however there will be group of {grpSmall} that will be left over. ")