def findMax(a,b):
    """Finds the maximum of two values."""
    if ( a > b ):
        max = a
    else:
        max = b
    return max

max_one = input("Input first value: ")
max_two = input("Input second value: ")

results = findMax(max_one, max_two)

print(f"The greater value is {results}")