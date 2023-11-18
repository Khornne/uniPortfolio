import math

roots = {n : math.sqrt(n) for n in range(1,26)}

for num,root in roots.items():
    print(f"The square root of {num} is {root}")