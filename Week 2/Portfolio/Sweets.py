total_sweets = int(input("How many sweets? "))
total_students = int(input("How many students attended? "))
divided_sweets = int(total_sweets / total_students)
leftover_sweets = total_sweets - (divided_sweets * total_students)

print(f"Each student will be given {divided_sweets} sweets and {leftover_sweets} sweets will be left over")

