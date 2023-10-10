Students = int(input("How many students? "))
reqGroup = int(input("Required group size? "))
grpTotal = int(Students / reqGroup)
smallGroup = Students - (grpTotal * reqGroup)

print(f"There will be {grpTotal} groups with {smallGroup} students left over.")
