def num_test(single_int):
    return 0 <= single_int <=100

numbers = int(input("Please enter a number: "))

result = num_test(numbers)
print(result)

