def calcAve(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total/len(numbers)

results = calcAve(10, 100)
print(results)